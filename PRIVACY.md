# Privacy notice

This skill package is published by **yuyun2000**. The repository distributes
instructions, documentation, examples and helper scripts; it does not operate
the M5Stack MCP or M5Burner services.

## Local use

Reading the bundled documentation and running the documentation finder do not
send their contents to a service operated by this repository. Your chosen AI
agent may send prompts, code and referenced files to its model provider under
that provider's settings and terms.

## External requests

- The M5Stack support skill and bundled MCP configuration connect to
  `https://mcp.m5stack.com/sse`. Search questions, answer requests and submitted
  feedback are sent to M5Stack. The support skill states that search and answer
  queries may be logged for service maintenance. Retention and access are
  controlled by the service operator.
- The firmware query CLI sends search filters and public catalog queries to
  `https://burner.m5stack.com`. Public queries do not require account tokens.
- Optional weather examples call external weather and IP-location services;
  inspect the specific example before running it.
- Installation through the third-party skills CLI can send installation
  telemetry to skills.sh. See its [telemetry documentation](https://github.com/vercel-labs/skills#telemetry);
  `DISABLE_TELEMETRY=1` disables that telemetry.

Do not include API keys, authorization headers, Wi-Fi passwords, customer data,
or other sensitive information in public queries, feedback or GitHub Issues.
Only submit feedback when authorized by the user. Public Issues and Discussions
are visible to other people. Privacy questions about this package can be raised
through a sanitized [repository Issue](https://github.com/yuyun2000/M5Stack-Skills/issues).
