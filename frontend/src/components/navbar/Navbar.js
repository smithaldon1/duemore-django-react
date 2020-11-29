import React from 'react';
import styled from 'styled-components';
import { useSpring, animated, config } from 'react-spring';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import Brand from './Brand';
import BurgerMenu from './BurgerMenu';
import CollapseMenu from './CollapseMenu';
import Home from '../home/Home';
import Features from '../Features';
import Pricing from '../Pricing';
import { Login } from '../login/Login';

const Navbar = (props) => {
    const barAnimation = useSpring({
        from: { transform: 'translate3d(0, -10rem, 0)' },
        transform: 'translate3d(0, 0, 0)',
    });

    const linkAnimation = useSpring({
        from: { transform: 'translate3d(0, 30px, 0)', opacity: 0 },
        to: { transform: 'translate3d(0, 0, 0)', opacity: 1 },
        delay: 800,
        config: config.wobbly,
    });

    return (
        <>
            <Router>
                <NavBar style={barAnimation}>
                    <FlexContainer>
                        <Brand />
                        <NavLinks style={linkAnimation}>
                                <a href="/">Home</a>
                                <a href="/features">Features</a>
                                <a href="/pricing">Pricing</a>
                                <a href="/login">Login</a>
                        </NavLinks>
                        <BurgerWrapper>
                            <BurgerMenu
                                navbarState={props.navbarState}
                                handleNavbar={props.handleNavbar}
                            />
                        </BurgerWrapper>
                    </FlexContainer>
                </NavBar>
                <CollapseMenu
                    navbarState={props.navbarState}
                    handleNavbar={props.handleNavbar}
                />
                <Switch>
                    <Route exact path='/'><Home /></Route>
                    <Route path='/features'><Features /></Route>
                    <Route path='/pricing'><Pricing /></Route>
                    <Route path='/login'><Login /></Route>
                </Switch>
            </Router>
        </>
    )
}

export default Navbar

const NavBar = styled(animated.nav)`
    position: fixed;
    width: 100%;
    top: 0;
    left: 0;
    background: #222831;
    z-index: 1;
    font-size: 1.4rem;
`;

const FlexContainer = styled.div`
    max-width: 120rem;
    display: flex;
    margin: auto;
    padding: 0 2rem;
    justify-content: space-between;
    height: 7rem;
`;

const NavLinks = styled(animated.ul)`
    justify-self: end;
    list-style-type: none;
    margin: auto 0;

    & a {
        color: #dfe6e9;
        text-transform: uppercase;
        font-weight: 600;
        border-bottom: 1px solid transparent;
        margin: 0 1.5rem;
        transition: all 300ms linear 0s;
        text-decoration: none;
        cursor: pointer;

        &:hover {
            color: #00adb5;
            border-bottom: 1px solid #00adb5;
        }

        @media (max-width: 768px) {
            display: none;
        }
    }
`;

const BurgerWrapper = styled.div`
    margin: auto 0;

    @media (min-width: 769px) {
        display: none;
    }
`;