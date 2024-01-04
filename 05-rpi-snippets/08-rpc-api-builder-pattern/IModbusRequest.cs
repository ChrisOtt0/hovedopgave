using MPC2.ModbusLib;
using MPC2.ModbusLib.Protocols;

namespace PMTester.Domain.Commands {
    public interface IModbusRequest {
        public bool Act { get; set; }
        public bool Dn { get; set; }
        public bool Err { get; set; }

        public Dictionary<int, object?> Payload { get; set; }
        public int Response { get; }

        public void Execute();
    }
}



namespace PMTester.Domain.Commands.Concretes {
    public abstract class AbstractModbusRequest : IModbusRequest {
        public bool Act { get; set; }
        public bool Dn { get; set; }
        public bool Err { get; set; }

        public Dictionary<int, object?> Payload { get; set; } = new Dictionary<int, object?>();
        public int Response { get; protected set; }


        protected ModbusClient? Driver => _owner.Driver;
        protected ICommClient? Port => _owner.PortClient;
        protected ModbusCommand _command;


        protected ModbusTcpMaster _owner;


        public abstract void Execute();


        protected void Clear() {
            Act = false;
            Dn = false;
            Err = false;
        }


        public AbstractModbusRequest(ModbusTcpMaster owner, ModbusCommand command) {
            _owner = owner;
            _command = command;
        }
    }
}
