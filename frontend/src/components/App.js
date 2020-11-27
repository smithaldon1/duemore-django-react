import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Switch, Route, NavLink } from 'react-router-dom';
import Features from './Features';
import Home from './Home';
import Pricing from './Pricing';
import TaskList from './TaskList';



export default class App extends React.Component {
    render() {
        return (
            <Router>
                <div>
                    <nav>
                        <ul>
                            <li><NavLink to="/">Home</NavLink></li>
                            <li><NavLink to="/features">Features</NavLink></li>
                            <li><NavLink to="/pricing">Pricing</NavLink></li>
                            <li><NavLink to="/tasks">Tasks</NavLink></li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/'><Home /></Route>
                        <Route path='/features'><Features /></Route>
                        <Route path='/pricing'><Pricing /></Route>
                        <Route path='/tasks'><TaskList /></Route>
                    </Switch>
                </div>
            </Router>
        );
    }
}

const container = document.getElementById("app");
render(
    <Router>
        <App />
    </Router>,
    container
);