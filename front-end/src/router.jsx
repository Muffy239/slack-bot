import App from "./App";
import { createBrowserRouter } from "react-router-dom";
import Login from "./pages/Login";
import NotFound from "./pages/NotFound";
import Home from "./pages/Home";
import Signup from "./pages/Signup";
import About from "./pages/About";
import { userConfirmation } from "../utilities";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        loader: userConfirmation,
        children: [
            {
                index: true,
                element: <Home />,
            },
            {
                path: "/about",
                element: <About />,
            },
            {
                path: "/login",
                element: <Login />,
            },
            {
                path: "/signup",
                element: <Signup />,
            },
            {
                path: "*",
                element: <NotFound />,
            },
        ],
        errorElement: <NotFound />,
    },
]);

export default router;
