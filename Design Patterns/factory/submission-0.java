interface Vehicle {
    String getType();
}

class Car implements Vehicle {
    @Override
    public String getType() {
        return "Car";
    }
}

class Bike implements Vehicle {
    @Override
    public String getType() {
        return "Bike";
    }
}

class Truck implements Vehicle {
    @Override
    public String getType() {
        return "Truck";
    }
}

abstract class VehicleFactory { // Creator
    abstract Vehicle createVehicle();
}

class CarFactory extends VehicleFactory { // Concrete Creators
    // Write your code here
    Vehicle createVehicle() {
        return new Car();
    }
}

class BikeFactory extends VehicleFactory { // Concrete Creators
    // Write your code here
    Vehicle createVehicle() {
        return new Bike();
    }
}

class TruckFactory extends VehicleFactory { // Concrete Creators
    // Write your code here
    Vehicle createVehicle() {
        return new Truck();
    }
}
