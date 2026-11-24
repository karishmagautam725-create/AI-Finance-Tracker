
import Home from "./component/Home"

import { BrowserRouter, Routes, Route } from "react-router-dom"
import Register from "./component/Register"
import Header from './component/Header'
import Footer from './component/Footer'
import Login from "./component/Login"
import AuthProvider from "./AuthProvider"
import Dashboard from "./pages/Dashboard"
// import { BarLoader } from "react-spinners"
// import { Suspense, lazy } from "react";
// Lazy Loader
// const Dashboard = lazy(() => import("./pages/Dashboard"));

function App() {


    return (
        <>
            <AuthProvider>
                <BrowserRouter >
                    <Header />
                    {/* <Suspense
                        fallback={
                            <BarLoader
                                className="mt-4"
                                width={"100%"}
                                color="#9333ea"
                            />
                        }
                    > */}
                        <Routes >
                            <Route path='/' element={<Home />} />
                            <Route path='/register' element={<Register />} />
                            <Route path='/login' element={<Login />} />
                            <Route path='/dashboard' element={

                                <Dashboard />

                            } />
                        </Routes >
                    {/* </Suspense> */}
                    <Footer />
                </BrowserRouter >

            </AuthProvider>
        </>
    )
}

export default App
