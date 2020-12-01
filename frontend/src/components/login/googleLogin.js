import axios from "axios";

const googleLogin = async (accessToken) => {
    let res = await axios.post(
        "http://localhost:8000/rest-auth/google/",
        {
            access_token : accessToken,
        }
    );
    console.log(res);
    return await res.status;
};

export default googleLogin;