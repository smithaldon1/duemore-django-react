import React, { Component } from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Link, Route, Switch } from 'react-router-dom';
import Dashboard from './Dashboard';
import HomePage from './Home';
import AccountPage from './Account';

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            tasks: [],
            loaded: false,
            placeholder: "Loading..."
        };
    }

    componentDidMount() {
        fetch("api/project")
            .then(response => {
                if (response.status > 400) {
                    return this.setState(() => {
                        return { placeholder: "Something went wrong! Please refresh the page."};
                    });
                }
                return response.json();
            })
            .then(tasks => {
                this.setState(() => {
                    return {
                        tasks,
                        loaded: true
                    };
                });
            });
    }

    render() {
        return (
            <>
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
                                    <Link to="/account">Account</Link>
                                </li>
                            </ul>
                        </nav>
                        <Switch>
                            <Route path="/dash">
                                <Dashboard />
                            </Route>
                            <Route path="/account">
                                <AccountPage />
                            </Route>
                            <Route exact path="/">
                                <HomePage />
                            </Route>
                        </Switch>
                    </div>
                </Router>
                <h2>Tasks</h2>
                <ul>
                    {this.state.tasks.map(task => {
                        return (
                            <li key={task.task_id}>
                                {task.name}
                                <ul>
                                    
                                    <li>{task.description}</li>
                                    <li>{task.start_date_time}</li>
                                    <li>{task.due_date_time}</li>
                                </ul>
                            </li>
                        );
                    })}
                </ul>
            </>
        )
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container)