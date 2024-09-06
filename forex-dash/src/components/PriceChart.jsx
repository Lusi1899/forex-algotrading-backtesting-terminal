import React, { useEffect, useState } from 'react'
import AccountSummary from'../components/AccountSummary'
import Headlines from'../components/Headlines'
import TitleHead from '../components/TitleHead'
import endPoints from "../app/api"
import Select from '../components/Select'
import Button from '../components/Button'
import Technicals from '../components/Technicals'
import { PAIRS, GRANULARITIES, COUNTS } from "../app/data"
import {drawChart} from "../app/chart"


function PriceChart({priceData, selectedPair, selectedGranularity, selectedCount,
handleCountChange}) {

useEffect(()=> {
if (priceData){
//console.log("Draw Chart",selectedPair,selectedGranularity);
drawChart(priceData, selectedPair, selectedGranularity, "chartDiv");

}
},[priceData]);

return(

    <div className="segment" id= "price-chart-holder">
   <Select
    name="numrows"
    title="Num. Rows."
    options={COUNTS}
    defaultValue={selectedCount}
    onSelected={handleCountChange}
   />
<div id="chartDiv"></div>
    </div>

)
}

export default PriceChart