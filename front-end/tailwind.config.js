/** @type {import('tailwindcss').Config} */
module.exports = {
    prefix: "tw-",
    content: ["./src/**/*.{html,js}"],
    theme: {
        extend: {
            colors: {
                "custom-gray": "#242424",
                "light-gray": "#F5F5F5",
            },
        },
    },
    plugins: [],
};

// /** @type {import('tailwindcss').Config} */
// export default {
//     content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
//     theme: {
//         extend: {
//             colors: {
//                 "custom-gray": "#242424",
//                 "light-gray": "#F5F5F5",
//             },
//         },
//     },
//     plugins: [],
// };
