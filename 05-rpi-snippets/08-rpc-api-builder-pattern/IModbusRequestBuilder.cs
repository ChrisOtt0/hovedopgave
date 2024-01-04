using MPC2.ModbusLib.Protocols;
using static PMTester.Domain.UpdatePatterns;

namespace PMTester.Domain.Commands.Builders;

public interface IModbusRequestBuilder {
    public void Reset();
    public void SetCommandType(ModbusCommand type);
    public void SetUpdateDelegate(UpdateDelegate? updateDelegate);
    public void SetOffset(int offset);
    public void SetCount(int count);
    public void SetData(ushort[] data);
    public void FinalizeRequest(ModbusTcpMaster owner);
    public IModbusRequest GetRequest();
}