class CheckInput:
    def check_alarm_input(alarm_time):
        """Checks to see if the user has entered in a valid alarm time"""
        if len(alarm_time) == 1: # [Hour] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0:
                return True
        if len(alarm_time) == 2: # [Hour:Minute] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0:
                return True
        elif len(alarm_time) == 3: #[Hour:Minute:Second] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0 and \
            alarm_time[2] < 60 and alarm_time[2] >= 0:
                return True
        return False