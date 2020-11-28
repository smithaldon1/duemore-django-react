import React, { Component } from 'react';
import { render } from 'react-dom';
import { library } from '@fortawesome/fontawesome-svg-core';
import { fab } from '@fortawesome/free-brands-svg-icons';
import { faCheckSquare, faCode, faCoffee } from '@fortawesome/free-solid-svg-icons';

import Navbar from './navbar/Navbar';
import Home from './home/Home';
import Features from './Features';
import Pricing from './Pricing';
import { Login } from './Login';

import GlobalStyle from '../styles/Global';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';


library.add(fab, faCode, faCheckSquare, faCoffee);

export default class App extends Component {
    state = {
        navbarOpen: false
    }

    handleNavbar = () => {
        this.setState({ navbarOpen: !this.state.navbarOpen });
    }

    render() {
        return (
            <>
                <Router>
                    <Navbar
                        navbarState={this.state.navbarOpen}
                        handleNavbar={this.handleNavbar}
                    />
                    <GlobalStyle />
                    {/* <Switch>
                        <Route exact path='/'><Home /></Route>
                        <Route path='/features'><Features /></Route>
                        <Route path='/pricing'><Pricing /></Route>
                        <Route path='/login'><Login /></Route>
                    </Switch> */}
                </Router>
            </>
        );
    }
}

const container = document.getElementById("app");
render(<App />, container);