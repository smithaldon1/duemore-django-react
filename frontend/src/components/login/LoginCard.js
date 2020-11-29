import React, { Component } from 'react'
import styled from 'styled-components';

const CardWrapper = styled.div`
    position: relative;
    top: 10rem;
    margin: auto;
    width: 75vw;
    height: 85vh;
    border: none;
    border-radius: 15px;
    box-shadow: -10px 10px 25px rgba(0,0,0,0.15), 10px -10px 25px #fff;
`;

const Card = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
`;


export default class LoginCard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            login: true
        }
    }

    render() {
        return (
            <CardWrapper>
                <Card>
                    <h1>Login Card</h1>
                </Card>
            </CardWrapper>
        )
    }
}
