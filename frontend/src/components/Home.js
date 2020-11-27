import React, { Component } from 'react';
import styled from 'styled-components';
import { device } from './device';

const NavBar = styled.nav`
    display
`;



export default class Home extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h1 className="header">Home Page</h1>
            </div>
        );
    }
}
