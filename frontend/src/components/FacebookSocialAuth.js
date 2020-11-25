import React, { Component } from 'react';
import FacebookLogin from 'react-facebook-login';

class FacebookSocialAuth extends Component {
    render() {
        const fbResponse = (response) => {
            console.log(response);
        }
        return (
            <div className="socialLoginBtn">
                <FacebookLogin 
                    textButton="LOGIN WITH FACEBOOK"
                    appId="1455548797983678"
                    fields="name,email,picture"
                    callback={fbResponse}
                />
            </div>
        );
    }
}

export default FacebookSocialAuth;