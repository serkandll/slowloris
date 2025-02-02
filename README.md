# Slowloris Toolkit

<img src="https://img.shields.io/badge/Python-3.8-blue"> <img src="https://img.shields.io/badge/Status-Beta-orange"> <img src="https://img.shields.io/badge/Version-4-red"> <img src="https://img.shields.io/badge/Licence-MIT-yellowgreen"> <a href="https://taguar258.github.io/Raven-Storm/INSTALLATION"><img src="https://img.shields.io/badge/Download-Now-green"></a>

**Slowloris is a powerful DDoS toolkit for penetration tests, including attacks for several protocols written in python(3.8).**

Takedown WiFi access points, devices in your network, servers, services, and Bluetooth devices with ease.

Raven(abbreviation) is desinged to help you to **test, understand, and learn from stress-testing** attacks.

Raven can **deal with strong servers** and **can be optimized** for non typical targets.

Raven will fit your purpose, even if it is **jamming down wifi networks or bluetooth devices**.

_I archived this repository because I currently do not want to work on it._

## What makes it different

- [x] Slowloris includes tools for creating shorcuts and working more efficiently.
- [x] Loris is **Effective** and **powerful** in shutting down hosts and servers.
- [x] **Testing** and understanding are the goals of Slowloris.
- [x] Loris lets you connects clients together to create a botnet.
- [x] Features different protocols such as UDP/TCP, ICMP, HTTP, L2CAP, ARP and IEEE.

## Installation

Just enter the following line to install Slowloris on Linux.

```bash
curl -s https://raw.githubusercontent.com/serkandll/slowloris/master/install.sh | sudo bash -s
```

<a style="color: grey" href="https://serkandll.github.io/slowloris/INSTALLATION"><b>Click here for the more detailed installation guide.</b></a>


<a style="color: grey" href="https://github.com/serkandll/slowloris/blob/master/README.md#info-and-warning"><b>Terms of Use</b></a>

<a style="color: grey" href="https://github.com/serkandll/slowloris/blob/master/LICENSE">Licence</a>

<a style="color: grey" href="https://github.com/serkandll/slowloris/projects/1">Project status/ToDo</a>

<a style="color: grey" href="https://github.com/serkandll/CLIF/">CLIF Framework</a>

## What module to use

| Method | Module  |
| ------- | --- |
| ping | l3 |
| udp/tcp services | l4 |
| websites | l7 |
| local devices | arp |
| bluetooth | bl |
| wifi | wifi |
| botnet | server |

_Try using the L4 attack if L7 fails._


## How to run a DDoS attack

_You probably already know the difference between DoS and DDoS:_
_A DoS Attack is run by a single Maschine and a DDoS Attack by multiple._

_But how do we perform a DDoS Attack using Slowloris?_


To connect multiple instances of Slowloris, you will then need to open a host.
Just execute the command `server` and define a custom password to prevent others from interfering.
When run, you will receive a URL that you can connect to when executing the `ddos` command.


## Info and Warning

__THE CREATOR (Serkan.dll) OF THE Slowloris TOOLKIT DOES NOT TAKE ANY RESPONSIBILITY FOR DAMAGE CAUSED. THE USER ALONE IS RESPONSIBLE, BE IT: ABUSING RAVEN-STORM TO FIT ILLEGAL PURPOSES OR ACCIDENTAL DAMAGE CAUSED BY Slowloris.
THE CREATOR DID NOT INTEND Slowloris AS A TOOL FOR ILLEGAL PURPOSES AND THEREFORE DOES NOT SUPPORT ANY ILLEGAL ABUSE OF THIS TOOL.
BY USING THIS SOFTWARE, YOU MUST AGREE TO TAKE FULL RESPONSIBILITY FOR DAMAGE CAUSED BY Slowloris IN ANY WAY ON YOUR OWN.
THE CREATOR DOES NOT WANT PEOPLE TO USE Slowloris IF THEY DO NOT HAVE EXPERIENCE WITH THE ATTACKS INCLUDED.
EVERY ATTACK WILL CAUSE TEMPORARY DAMAGE, BUT LONG-TERM DAMAGE IS DEFFINITIFLY POSSIBLE.
Slowloris SHOULD NOT SUGGEST PEOPLE TO PERFORM ILLEGAL ACTIVITIES.__

__THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.__

**MIT serkandll 2020**

