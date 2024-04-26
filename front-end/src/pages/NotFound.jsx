import { Link } from "react-router-dom";

const NotFound = () => {
    return (
        <>
            <div id="Container" className="w-full h-screen">
                <h1>You've accessed an unknown page.</h1>
                <Link to={"/"}>Home</Link>
            </div>
        </>
    );
};

export default NotFound;
