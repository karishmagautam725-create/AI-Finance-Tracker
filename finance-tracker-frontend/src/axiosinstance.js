import axios from "axios";

const baseURL = import.meta.env.VITE_BACKEND_BASE_API;

const axiosInstance = axios.create({
    baseURL,
    headers: {
        "Content-Type": "application/json",
    },
});

// Separate instance
const refreshAxios = axios.create({
    baseURL,
});

// Request Interceptor
axiosInstance.interceptors.request.use(
    (config) => {
        const accessToken = localStorage.getItem("accessToken");

        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
        }

        return config;
    },
    (error) => Promise.reject(error)
);

// Response Interceptor
axiosInstance.interceptors.response.use(
    (response) => response,

    async (error) => {
        const originalRequest = error.config;

        if (
            error?.response?.status === 401 &&
            !originalRequest._retry &&
            originalRequest.url !== "/api/token/refresh/"
        ) {
            originalRequest._retry = true;

            const refreshToken = localStorage.getItem("refreshToken");

            try {
                const response = await refreshAxios.post(
                    "/api/token/refresh/",
                    {
                        refresh: refreshToken,
                    }
                );
                console.log('New Access Token=>',response.data.access) 
                const newAccessToken = response.data.access;

                localStorage.setItem(
                    "accessToken",
                    newAccessToken
                );

                originalRequest.headers.Authorization =
                    `Bearer ${newAccessToken}`;

                return axiosInstance(originalRequest);

            } catch (refreshError) {

                localStorage.removeItem("accessToken");
                localStorage.removeItem("refreshToken");

                window.location.href = "/login";

                return Promise.reject(refreshError);
            }
        }

        return Promise.reject(error);
    }
);

export default axiosInstance;