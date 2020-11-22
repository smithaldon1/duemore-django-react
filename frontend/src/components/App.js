import React, { Component } from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom';
import Dashboard from './Dashboard';
import HomePage from './Home';
import AccountPage from './Account';
import TaskPage from './TaskPage';
import ProjectsPage from './ProjectsPage';
import FiltersPage from './FiltersPage';
import SettingsPage from './SettingsPage';

class App extends Component {
    constructor(props) {
        super(props);
        
    }

    render() {
        return (
            <Router>
                <div>
                    <nav>
                        <ul>
                            <li>
                                <Link to="/">Home</Link>
                            </li>
                            <li>
                                <Link to="/dash">Dashboard</Link>
                            </li>
                            <li>
                                <Link to="/tasks">Tasks</Link>
                            </li>
                            <li>
                                <Link to="/projects">Projects</Link>
                            </li>
                            <li>
                                <Link to="/filters">Filters</Link>
                            </li>
                            <li>
                                <Link to="/account">Account</Link>
                            </li>
                            <li>
                                <Link to="/settings">Settings</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path="/">
                            <HomePage />
                        </Route>
                        <Route path="/dash">
                            <Dashboard />
                        </Route>
                        <Route path="/tasks">
                            <TaskPage />
                        </Route>
                        <Route path="/projects">
                            <ProjectsPage />
                        </Route>
                        <Route path="/filters">
                            <FiltersPage />
                        </Route>
                        <Route path="/account">
                            <AccountPage />
                        </Route>
                        <Route path="/settings">
                            <SettingsPage />
                        </Route>
                    </Switch>
                </div>
            </Router>
        )
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container)