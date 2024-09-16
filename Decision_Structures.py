def calculate_time_saved(speed, speed_limit, distance):
    # Time taken at the given average speed
    time_at_speed = distance / speed
    
    # Time taken at the speed limit
    time_at_speed_limit = distance / speed_limit
    
    # Calculate the time saved in hours
    time_saved_hours = time_at_speed_limit - time_at_speed
    
    # Convert time saved to minutes
    time_saved_minutes = time_saved_hours * 60
    
    return time_saved_minutes

def main():
    try:
        # Get user inputs
        speed = float(input("Enter your average speed (in miles per hour): "))
        speed_limit = float(input("Enter the speed limit (in miles per hour): "))
        distance = float(input("Enter the distance traveled (in miles): "))

        # Ensure the speed is greater than the speed limit
        if speed <= speed_limit:
            print("Your average speed should be greater than the speed limit.")
            return
        
        # Calculate time saved
        time_saved = calculate_time_saved(speed, speed_limit, distance)
        
        # Output the result
        print(f"Time saved by traveling at {speed} mph instead of {speed_limit} mph over {distance} miles is {time_saved:.2f} minutes.")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for speed, speed limit, and distance.")
    
if __name__ == "__main__":
    main()
