import "./App.css";
import { Outlet } from "react-router-dom";
import * as React from "react";
import NavBar from "./components/NavBar";
import "bootstrap/dist/css/bootstrap.min.css";

// import { useEffect } from "react";
// import axios from "axios";

function App() {
    //* TESTING
    // const testConnection = async () => {
    //     let response = await axios.get("http://127.0.0.1:8000/api/test/");
    //     console.log(response);
    // };

    // useEffect(() => {
    //     testConnection();
    // }, []);

    return (
        <>
            <NavBar />
            <Outlet />
        </>
    );
}

export default App;
