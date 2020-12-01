import axios from 'axios';

const fbLogin = async (accesstoken) => {
    let res = await axios.post(
        "http://localhost:8000/rest-auth/facebook/",
        {
            access_token : accesstoken,
        }
    );
    console.log(res);
    return await res.status;
};

export default fbLogin;