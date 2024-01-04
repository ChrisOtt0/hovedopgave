using MPC2.ModbusLib;
using MPC2.ModbusLib.Protocols;
using static PMTester.Domain.UpdatePatterns;

namespace PMTester.Domain.Commands.Concretes;

public class ModbusReadRequest : AbstractModbusRequest
{
    private UpdateDelegate Update;

    public override void Execute()
    {
        Clear();

        try {
            Act = true;

            if (Driver != null && Port != null) {
                var _result = Driver.ExecuteGeneric(Port, _command);
                Response = _result.Status;

                if (_result.Status == CommResponse.Ack) {
                    Err = !Update(_command.Data, out Dictionary<int, object?> payload);
                    if (Err) return;

                    Payload = payload;
                }
                else {
                    Err = true;
                    return;
                }

                Dn = true;
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

    public ModbusReadRequest(ModbusTcpMaster owner, ModbusCommand command, UpdateDelegate updateFunc) 
        : base(owner, command) {
            Update = updateFunc;
        }
}