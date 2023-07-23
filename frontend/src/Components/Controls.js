import React from "react";
import "./Controls.css";

const Controls = ({fetchMaze}) =>{
    return(
        <div className="controls">
            <div id="maze_generator" onClick={fetchMaze}>Generate Maze</div>
            <div id="algorithm_slct">Select Algorithm</div>
            <div id="start">Start</div>
            <div id="clear">Clear</div>
        </div>
    )
}
export default Controls;