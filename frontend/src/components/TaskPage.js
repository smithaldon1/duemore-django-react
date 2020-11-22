import React, { Component } from 'react'

export default class TaskPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            tasks: [],
            loaded: false,
            placeholder: ''
        }
    }

    componentDidMount() {
        fetch("api/task")
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
            <div>
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
            </div>
        );
    }
}