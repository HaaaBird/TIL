const { WelstoryClient } = require('..')

;(async () => {
  const client = new WelstoryClient()

  const loginResult = await client.login({
    username: "thinkingong1",
    password: "Tkvl1234@",
  })

  console.log(loginResult)

  const refreshAfter = await client.refreshSession()
  console.log(`Session needed to be refreshed after ${refreshAfter}s`)
})()
