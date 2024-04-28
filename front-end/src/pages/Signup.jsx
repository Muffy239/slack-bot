import React, { useState } from "react";
import { api } from "../../utilities";

const Signup = () => {
    // Setting up state for the email
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [displayname, setDisplayName] = useState("");

    // Handler to update the state when the input changes
    const handleEmailChange = (event) => {
        setEmail(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleDisplayName = (event) => {
        setDisplayName(event.target.value);
    };

    const signupUser = async (e) => {
        e.preventDefault();
        const response = await api.post("users/signup/", { email: email, password: password, display_name: displayname });
        if (response.status === 201) {
            console.log("successful sign up, user info", response.data);
            const { token, user } = response.data;
            // save auth token so it can be used
            localStorage.setItem("token", token);
            api.defaults.headers.common["Authorization"] = `Token ${token}`;
            // set user info for the app
            setUser({ email: email, user });
        }
    };

    return (
        <>
            <div className="d-flex justify-content-center align-items-center min-vh-100 tw-bg-light-gray">
                <form className="w-100 max-w-lg bg-white shadow-lg rounded px-4 pt-3 pb-3 mb-4" onSubmit={signupUser}>
                    <div className="mb-3">
                        <label htmlFor="staticEmail" className="form-label tw-text-gray-700 tw-text-sm tw-font-bold tw-mb-2">
                            Display Name
                        </label>
                        <input type="text" className="form-control tw-border tw-rounded tw-w-full tw-py-2 tw-px-3 tw-text-gray-700 tw-leading-tight tw-focus:outline-none tw-focus:shadow-outline" placeholder="Username0239" value={displayname} onChange={handleDisplayName} />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="staticEmail" className="form-label tw-text-gray-700 tw-text-sm tw-font-bold tw-mb-2">
                            Email
                        </label>
                        <input type="text" className="form-control tw-border tw-rounded tw-w-full tw-py-2 tw-px-3 tw-text-gray-700 tw-leading-tight tw-focus:outline-none tw-focus:shadow-outline" placeholder="email@example.com" value={email} onChange={handleEmailChange} />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="inputPassword" className="form-label tw-text-gray-700 tw-text-sm tw-font-bold tw-mb-2">
                            Password
                        </label>
                        <input type="password" className="form-control tw-border tw-rounded tw-w-full tw-py-2 tw-px-3 tw-text-gray-700 tw-mb-3 tw-leading-tight tw-focus:outline-none tw-focus:shadow-outline" id="inputPassword" placeholder="Password" value={password} onChange={handlePasswordChange} />
                    </div>
                    <div className="d-flex justify-content-between align-items-center">
                        <button className="btn btn-primary tw-bg-blue-500 tw-hover:bg-blue-700 tw-text-white tw-font-bold tw-py-2 tw-px-4 tw-rounded tw-focus:outline-none tw-focus:shadow-outline" type="submit">
                            Submit form
                        </button>
                    </div>
                </form>
            </div>
        </>
    );
};

export default Signup;
