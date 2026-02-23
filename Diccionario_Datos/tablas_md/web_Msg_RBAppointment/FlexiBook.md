# web_Msg_RBAppointment.FlexiBook

**Schema:** web_Msg_RBAppointment
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Agenda de Citas (Web)**. Interfaz de agendamiento de consultas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ASSIDR | bigint |  | FK | SI | - |
| AdmDR | bigint |  | FK | SI | - |
| Age | integer |  |  | SI | - |
| ApptEndTime | time |  |  | SI | - |
| AuxInsTypeDR | bigint |  | FK | SI | - |
| BulkApptDur | integer |  |  | SI | - |
| BulkApptList | varchar |  |  | SI | - |
| BulkApptListNonCycle | varchar |  |  | SI | - |
| CareProvDR | varchar |  | FK | SI | - |
| CareProvId | varchar |  |  | SI | - |
| ClinicalGrpDR | bigint |  | FK | SI | - |
| ConsecDays | varchar |  |  | SI | - |
| ConsecDressTime | varchar |  |  | SI | - |
| ConsultCategDR | bigint |  | FK | SI | - |
| Date | date |  |  | SI | - |
| DateOfOnset | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| DaysDuration | integer |  |  | SI | - |
| DaysOfWeek | varchar |  |  | SI | - |
| DiaryHeight | integer |  |  | SI | - |
| DiaryWidth | integer |  |  | SI | - |
| DiaryX | integer |  |  | SI | - |
| DiaryY | integer |  |  | SI | - |
| DoFind | bit |  |  | SI | - |
| EBookerEntityDR | bigint |  | FK | SI | - |
| EBookerPrioritiesSelected | varchar |  |  | SI | - |
| EndTime | time |  |  | SI | - |
| EqDR | bigint |  | FK | SI | - |
| FirstAvailableOnGrid | varchar |  |  | SI | - |
| FreeTextReasonTTG | varchar |  |  | SI | - |
| Frequency | integer |  |  | SI | - |
| FrequencyUnit | varchar |  |  | SI | - |
| GridOverbook | varchar |  |  | SI | - |
| GroupNumberDR | varchar |  | FK | SI | - |
| HCADR | bigint |  | FK | SI | - |
| Hospitals | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InsTypeDR | bigint |  | FK | SI | - |
| InterpreterDR | bigint |  | FK | SI | - |
| LocationDR | bigint |  | FK | SI | - |
| MultiSelect | varchar |  |  | SI | - |
| NationalCode | varchar |  |  | SI | - |
| NumberPerWeek | integer |  |  | SI | - |
| OEOrdItemIDs | varchar |  |  | SI | - |
| OneDayOnly | varchar |  |  | SI | If set to Y then the Date field serves as both Dat... |
| OperRoomID | bigint |  |  | SI | - |
| PAPMIDR | bigint |  | FK | SI | - |
| Payors | varchar |  |  | SI | - |
| PercentIncrDur | numeric |  |  | SI | - |
| Plans | varchar |  |  | SI | - |
| QUICK | bit |  |  | SI | - |
| RESLOCx | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| ReasonBreachDR | bigint |  | FK | SI | - |
| Remarks | varchar |  |  | SI | - |
| ResourceDR | bigint |  | FK | SI | - |
| Rows | integer |  |  | SI | - |
| SSServiceSetDR | bigint |  | FK | SI | - |
| ServDuration | integer |  |  | SI | - |
| SessTypes | varchar |  |  | SI | - |
| SessTypesSelected | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SessionLabels | varchar |  |  | SI | - |
| SexDR | bigint |  | FK | SI | - |
| SingleTransApptDR | varchar |  | FK | SI | - |
| StartTime | time |  |  | SI | - |
| TotalToBeBooked | integer |  |  | SI | - |
| TransApptServList | varchar |  |  | SI | - |
| TransportComments | varchar |  |  | SI | - |
| TransportDR | bigint |  | FK | SI | - |
| UserViewing | varchar |  |  | SI | - |
| WaitingListDR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |
| chkActivity | varchar |  |  | SI | - |
| chkAdjacentTimes | varchar |  |  | SI | - |
| chkAllResFlag | varchar |  |  | SI | - |
| chkAllTimes | varchar |  |  | SI | - |
| chkApptLetter | varchar |  |  | SI | - |
| chkConsecTimesRes | varchar |  |  | SI | - |
| chkConsecutiveTimes | varchar |  |  | SI | - |
| chkEditLetter | varchar |  |  | SI | - |
| chkFri | varchar |  |  | SI | - |
| chkGroupSameDay | varchar |  |  | SI | - |
| chkInfectious | varchar |  |  | SI | - |
| chkInterpreterRequired | varchar |  |  | SI | - |
| chkLinkResource | varchar |  |  | SI | - |
| chkMon | varchar |  |  | SI | - |
| chkPrintGPLetter | varchar |  |  | SI | - |
| chkPrintLater | varchar |  |  | SI | - |
| chkPrintPatientLetter | varchar |  |  | SI | - |
| chkSTimeED | varchar |  |  | SI | - |
| chkSameTime | varchar |  |  | SI | - |
| chkSat | varchar |  |  | SI | - |
| chkSun | varchar |  |  | SI | - |
| chkThu | varchar |  |  | SI | - |
| chkTransportRequired | varchar |  |  | SI | - |
| chkTue | varchar |  |  | SI | - |
| chkWed | varchar |  |  | SI | - |
| chkgrpAppt | varchar |  |  | SI | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*