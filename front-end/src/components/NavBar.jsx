import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";

function NavBar() {
    return (
        <div className="flex justify-between items-center w-full">
            <Navbar expand="lg" className="w-full">
                <Container className="flex justify-between items-center w-full">
                    <Navbar.Brand href="/" className="flex-grow-0">
                        Slack Bot
                    </Navbar.Brand>
                    <div className="flex-grow">
                        <Navbar.Toggle aria-controls="basic-navbar-nav" />
                        <Navbar.Collapse id="basic-navbar-nav">
                            <Nav className="ml-auto">
                                <Nav.Link href="/">Home</Nav.Link>
                                <Nav.Link href="/about">About</Nav.Link>
                                <NavDropdown title="Account" id="basic-nav-dropdown">
                                    <NavDropdown.Item href="/signup">Signup</NavDropdown.Item>
                                    <NavDropdown.Item href="/login">Login</NavDropdown.Item>
                                </NavDropdown>
                            </Nav>
                        </Navbar.Collapse>
                    </div>
                </Container>
            </Navbar>
        </div>
    );
}

export default NavBar;
