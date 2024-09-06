import React from 'react'
import AccountSummary from'../components/AccountSummary'
import Headlines from'../components/Headlines'
const HEADERS=[
   "R1", "R2", "R3",'S3', 'S2', 'S1', 'Pivot Point'
];



function Technicals({data}) {
return(

<div className="segment">
<div className="tech-header">
{data["Currency_Pair"]}
</div >
       <div className="tech-data">
    <div
        className="tech-summary"
        style={{
            background: data["Summary"] === "Sell" || data["Summary"] === "Strong Sell"
                ? "rgb(255, 80, 80)"
                : data["Summary"] === "Buy" || data["Summary"] === "Strong Buy"
                ? "rgb(9, 145, 11)"
                : "inherit"
        }}
    >
        Summary: {data["Summary"]}
    </div>

    <div className="tech-summary"
       style={{
            background: data["Moving Average"] === "Sell" || data["Moving Average"] === "Strong Sell"
                ? "rgb(255, 80, 80)"
                : data["Moving Average"] === "Buy" || data["Moving Average"] === "Strong Buy"
                ? "rgb(9, 145, 11)"
                : "inherit"
        }}
    >
        Moving Averages: {data["Moving Average"]}
    </div>

    <div className="tech-summary"
     style={{
            background: data["Indicator"] === "Sell" || data["Indicator"] === "Strong Sell"
                ? "rgb(255, 80, 80)"
                : data["Indicator"] === "Buy" || data["Indicator"] === "Strong Buy"
                ? "rgb(9, 145, 11)"
                : "inherit"
        }}

    >
        Indicators: {data["Indicator"]}
    </div>
</div>

<div className="tech-table">
<table>
    <thead>
        <tr>
            {
            HEADERS.map(item=>{
            return <th key={item}>{item}</th>
            }
            )
            }
        </tr>

        <tr>
            {
            HEADERS.map(item=>{
            return <td key={item}>{data[item]}</td>
            }

            )
            }
        </tr>

    </thead>
</table>

</div>
</div>

)
}

export default Technicals