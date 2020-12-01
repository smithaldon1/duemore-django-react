import React, { Component } from 'react';
import styled from 'styled-components';
import FacebookLoginWithButton from 'react-facebook-login';
import { GoogleLogin } from 'react-google-login';
import fbLogin from './fbLogin';
import googleLogin from './googleLogin';

const clientId = '777894477378-cubvk97fer39p9m85rr46j926klhj8gk.apps.googleusercontent.com';

const CardWrapper = styled.div`
    position: relative;
    top: 10rem;
    margin: auto;
    width: 75vw;
    height: 85vh;
    border: none;
    border-radius: 15px;
    box-shadow: -10px 10px 25px rgba(0,0,0,0.15), 10px -10px 25px #fff;
    display: flex;
    align-items: center;
    justify-content: center;
`;

const Card = styled.div`
    display: flex;
    flex-direction: column;
`;



export default class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            login: true
        }
    }

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
            <CardWrapper>
                <Card>
                    <FacebookLoginWithButton
                        appId="1455548797983678"
                        fields="name,email,picture"
                        callback={responseFacebook}
                        icon="fa-facebook"
                    />
                    <br/>
                    <br/>
                    <GoogleLogin
                        clientId={clientId}
                        buttonText="Login with Google"
                        onSuccess={responseGoogle}
                        onFailure={responseGoogle}
                        cookiePolicy={'single_host_origin'}
                        style={{ marginTop: '20px' }}
                    />
                </Card>
            </CardWrapper>
        )
    }
}
