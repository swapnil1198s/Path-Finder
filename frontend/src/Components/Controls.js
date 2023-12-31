import React from "react";
import "./Controls.css";

const Controls = ({fetchMap, clearMap}) =>{
    return(
        <div className="controls">
            <div id="map_generator" onClick={fetchMap}>Generate Map</div>
            <div id="algorithm_slct">Select Algorithm</div>
            <div id="start">Start</div>
            <div id="clear" onClick={clearMap}>Clear Map</div>
        </div>
    )
}
export default Controls;