import React, { Component } from 'react';
import GoogleLogin from 'react-google-login';

class GoogleSocialAuth extends Component {

    render() {
        const googleResponse = (response) => {
            console.log(response);
        }
        return (
            <div className="socialLoginBtn">
                <GoogleLogin
                    clientId="777894477378-cubvk97fer39p9m85rr46j926klhj8gk.apps.googleusercontent.com"
                    buttonText="LOGIN WITH GOOGLE"
                    onSuccess={googleResponse}
                    onFailure={googleResponse}
                />
            </div>
        );
    }
}

export default GoogleSocialAuth;