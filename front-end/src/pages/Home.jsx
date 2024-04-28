import { useOutletContext } from "react-router-dom";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import { Nav } from "react-bootstrap";

const Home = () => {
    const { user, setUser } = useOutletContext();

    return (
        <div id="Container" className="w-full h-screen bg-light-gray">
            <h3>Home</h3>
            {user ? (
                <>
                    <h3>Logged In</h3> <Button href="https://www.google.com/">Slack</Button>
                </>
            ) : (
                <h3>Sign up or Log In </h3>
            )}
        </div>
    );
};

export default Home;
