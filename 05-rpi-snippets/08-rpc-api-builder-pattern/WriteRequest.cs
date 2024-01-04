using MPC2.ModbusLib;
using MPC2.ModbusLib.Protocols;

namespace PMTester.Domain.Commands.Concretes;

public class ModbusWriteRequest : AbstractModbusRequest {
    public override void Execute() {
        Clear();

        try {
            Act = true;

            if (Driver != null && Port != null) {
                var i_Result = Driver.ExecuteGeneric(Port, _command);
                Response = i_Result.Status;
                if (i_Result.Status == CommResponse.Ack) {
                    Dn = true;
                }
                else {
                    Err = true;
                }
            }
            else {
                Err = true;
            }
        }
        catch {
            Err = true;
        }
        finally {
            Act = false;
        }
    }

    public ModbusWriteRequest(ModbusTcpMaster owner, ModbusCommand command) : base(owner, command) {}
}