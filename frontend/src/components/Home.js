import React, { Component } from 'react';
import styled from 'styled-components';

export default class Home extends Component {
    constructor(props) {
        super(props);
    }

    const Button = styled.button`
        background: ${props => props.primary ? "white" : "palevioletred"};
        color: ${props => props.primary ? "palevioletred" : "white"};
        font-size: 1em;
        margin: 2em;
        padding: 0.5em 1.25em;
        border: 2px solid palevioletred;
        border-radius: 10px;
    `;

    render() {
        return (
            <div>
                <h1 className="header">Home Page</h1>
                <Button>Normal</Button>
                <Button primary>Primary</Button>
            </div>
        )
    }
}
