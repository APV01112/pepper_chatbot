import qi
import argparse
import sys
import ask

def main(session):
    """
    This example uses the ALTextToSpeech service to make Pepper say something.
    """
    # Get the ALTextToSpeech service.
    tts = session.service("ALTextToSpeech")
    while True:
        user_input = input("User: ")
        tts.say(ask.question(user_input))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.137.197",
                        help="Robot IP address. On robot or Local Naoqi: use '192.168.137.197")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at IP \"" + args.ip + "\" on port " + str(args.port) + ".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)