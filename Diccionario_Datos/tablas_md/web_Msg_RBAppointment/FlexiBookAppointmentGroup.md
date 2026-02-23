# web_Msg_RBAppointment.FlexiBookAppointmentGroup

**Schema:** web_Msg_RBAppointment
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AppointMethodDR | bigint |  | FK | SI | - |
| AuxInsTypeDR | bigint |  | FK | SI | - |
| CareProvDR | varchar |  | FK | SI | - |
| ComputedLocationDR | bigint |  | FK | SI | - |
| ComputedResourceDR | bigint |  | FK | SI | - |
| ComputedServiceDR | bigint |  | FK | SI | - |
| ComputedServiceGroupDR | bigint |  | FK | SI | - |
| ConsultCategDR | bigint |  | FK | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| DaysDuration | integer |  |  | SI | - |
| DisableInterpreter | bit |  |  | SI | - |
| DisableTransport | bit |  |  | SI | - |
| DoctorLetterNotes | varchar |  |  | SI | - |
| EqDR | bigint |  | FK | SI | - |
| ExtDocFiscalCode | varchar |  |  | SI | - |
| ExtPaperPrescNo | varchar |  |  | SI | - |
| ExtPrescID | varchar |  |  | SI | - |
| ExtraFieldText1 | varchar |  |  | SI | - |
| ExtraFieldText10 | varchar |  |  | SI | - |
| ExtraFieldText2 | varchar |  |  | SI | - |
| ExtraFieldText3 | varchar |  |  | SI | - |
| ExtraFieldText4 | varchar |  |  | SI | - |
| ExtraFieldText5 | varchar |  |  | SI | - |
| ExtraFieldText6 | varchar |  |  | SI | - |
| ExtraFieldText7 | varchar |  |  | SI | - |
| ExtraFieldText8 | varchar |  |  | SI | - |
| ExtraFieldText9 | varchar |  |  | SI | - |
| FirstAvailable | varchar |  |  | SI | - |
| Frequency | integer |  |  | SI | - |
| FrequencyUnit | varchar |  |  | SI | - |
| FromSlotLocationDR | bigint |  | FK | SI | - |
| FromSlotResourceDR | bigint |  | FK | SI | - |
| FromSlotServiceDR | bigint |  | FK | SI | - |
| FromSlotServiceGroupDR | bigint |  | FK | SI | - |
| GroupDescription | varchar |  |  | SI | - |
| GroupNumberDR | varchar |  | FK | SI | - |
| HCADR | bigint |  | FK | SI | - |
| HospIDs | varchar |  |  | SI | - |
| Hospitals | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InsTypeDR | bigint |  | FK | SI | - |
| InterpreterDR | bigint |  | FK | SI | - |
| ItemGroup | varchar |  |  | SI | - |
| LocationDR | bigint |  | FK | SI | - |
| NumberPerWeek | integer |  |  | SI | - |
| NumberSelected | numeric |  |  | SI | - |
| OBReasonDR | bigint |  | FK | SI | - |
| OrderItemDR | varchar |  | FK | SI | - |
| PAPMIDR | bigint |  | FK | SI | - |
| ParRef | varchar |  |  | SI | - |
| PatientLetterNotes | varchar |  |  | SI | - |
| PreferredLanguageDR | bigint |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| Remarks | varchar |  |  | SI | - |
| ResourceDR | bigint |  | FK | SI | - |
| RoomDR | bigint |  | FK | SI | - |
| SSMain | varchar |  |  | SI | - |
| SSNoOfDays | numeric |  |  | SI | - |
| SSSeq | numeric |  |  | SI | - |
| SSServiceSetDR | bigint |  | FK | SI | - |
| SequenceOrder | varchar |  |  | SI | - |
| ServiceDR | bigint |  | FK | SI | - |
| ServiceGroupDR | bigint |  | FK | SI | - |
| SessionId | varchar |  |  | SI | - |
| SessionTypeDR | bigint |  | FK | SI | - |
| TotalToBeBooked | integer |  |  | SI | - |
| TransApptDR | varchar |  | FK | SI | - |
| TransportComments | varchar |  |  | SI | - |
| TransportDR | bigint |  | FK | SI | - |
| Urgent | varchar |  |  | SI | - |
| WaitingListDR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |
| chkApptLocAll | varchar |  |  | SI | - |
| chkAutoReq | varchar |  |  | SI | - |
| chkIncapacity | varchar |  |  | SI | - |
| chkIncludeInSearch | varchar |  |  | SI | - |
| chkInterpreterRequired | varchar |  |  | SI | - |
| chkTransportRequired | varchar |  |  | SI | - |
| duration | numeric |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*