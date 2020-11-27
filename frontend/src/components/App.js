import React, { Component } from 'react';
import { render } from 'react-dom';


class App extends Component {
    state = {
        tasks: [],
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://127.0.0.1:8000/api/task/');
            const tasks = await res.json();
            this.setState({
                tasks
            });
        } catch (e) {
            console.log(e)
        }
    }

    render() {
        return (
            <div>
                {this.state.tasks.map(item => (
                    <div key={item.task_id}>
                        <h1>{item.name}</h1>
                        <p>{item.description}</p>
                        <p>{item.start_date_time}</p>
                        <p>{item.due_date_time}</p>
                        <p>{item.priority}</p>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container)