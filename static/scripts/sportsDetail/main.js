function showScore(elem) {
    const score = document.getElementById(elem)
    score.style.color = 'black'
    score.style.textShadow = 'none'
}

function showAllScores() {
    const scores = document.getElementsByClassName('score')
    Array.from(scores).forEach((score) => {
        score.style.color = 'black'
        score.style.textShadow = 'none'
    });
}

const leagueObj = {
    '4424':'Chicago Cubs',
    '4387': 'MAVS',
    '4380': 'NYR',
    '4391': 'CAR',
    '4328': 'TOTTENHAM'
}

function highlightTeam() {
    const id = document.getElementById('league-id')
    if (id.value == '4328'){
        const row = document.getElementById('Tottenham')
        row.style.background = '#72d3fe'
    }
    else if (id.value == '4387') {
        findTeam('DAL')

    }
    else if (id.value == '4391') {
        findTeam('CAR')

    }
    else if (id.value == '4380') {
        findTeam('NYR')
    }
    else if (id.value == '4424') {
        findTeam('CHC')
}}

function worthWatching() {
    let allScores = []
    const teams = {'MAVS': {'delta': 5 , 'min': 70},
     'CUBS': {'delta': 2 , 'min': 0}, 'TOTTENHAM' :{ 'delta': 1 , 'min': 0}, 'NYR' : {'delta': 2 , 'min': 1}, 'PAN': {'delta': 7 , 'min': 6} }
    // get teams and scores

    for (let counter = 1; counter < 6; counter++) {
        const homeTeam = document.getElementById(`home-team-${counter}`)
        const awayTeam = document.getElementById(`away-team-${counter}`)

        const homeScore = parseInt(document.getElementById(`home-score-${counter}`).innerHTML)
        const awayScore = parseInt(document.getElementById(`away-score-${counter}`).innerHTML)

        // home games
        if (teams[homeTeam.innerHTML]) {
            const team = teams[homeTeam.innerHTML]
            const lossMargin = awayScore - homeScore

            if (homeScore >= awayScore && homeScore > team.min ) {

                homeTeam.parentNode.style.background = '#72d3fe'
            }
            else if (lossMargin <= team.delta) {
                homeTeam.parentNode.style.background = '#72d3fe'
            }
        }
        // away games
        else {
            const team = teams[awayTeam.innerHTML]
            const lossMargin = homeScore - awayScore
            console.log(homeTeam)
            console.log(awayTeam)
            if (awayScore >= homeScore && awayScore > team.min) {
                awayTeam.parentNode.style.background = '#72d3fe'

            }
            else if (lossMargin <= team.delta) {
                awayTeam.parentNode.style.background = '#72d3fe'
            }
        }
    }
}

highlightTeam()


function findTeam(teamName) {

    const aTags = document.getElementsByTagName('a')
        Array.from(aTags).forEach((tag) => {
            if (tag.innerHTML == teamName) {
                const row = tag.parentNode.parentNode
                row.style.background = '#72d3fe'

            }
        });

}