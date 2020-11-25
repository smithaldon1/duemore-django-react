import React, { Component } from 'react';
import FacebookLogin from 'react-facebook-login';
import GoogleLogin from 'react-google-login';
import fbLogin from '../services/fbLoginService';
import googleLogin from '../services/googleLoginService';

class LoginPage extends Component {
    render() {
        const responseFacebook = async (response) => {
            let fbResponse = await fbLogin(response.accessToken)
            console.log(fbResponse);
            console.log(response);
        }

        const responseGoogle = async (response) => {
            let googleResponse = await googleLogin(response.accessToken)
            console.log(googleResponse);
            console.log(response);
        }

        return (
            <div className="login_div">
                <FacebookLogin
                    textButton="LOGIN WITH FACEBOOK"
                    appId="1455548797983678"
                    fields="name,email,picture"
                    callback={responseFacebook}  
                />
                <br/>
                <br/>
                <GoogleLogin
                    clientId="777894477378-cubvk97fer39p9m85rr46j926klhj8gk.apps.googleusercontent.com"
                    buttonText="LOGIN WITH GOOGLE"
                    onSuccess={responseGoogle}
                    onFailure={responseGoogle}
                />
            </div>
        )
    }
}

export default LoginPage;