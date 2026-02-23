# SQLUser.SS_HL7

**Schema:** SQLUser
**Columnas:** 45
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HL7_RowId | varchar | PK |  | NO | - |
| HL7_ACKApplication | varchar |  |  | SI | Sending Application for ACK to inbound msg |
| HL7_ACKFacility | varchar |  |  | SI | Sending facility for ACK to inbound msg |
| HL7_AutoStartOutbound | varchar |  |  | SI | Auto start outbound interface |
| HL7_Code | varchar |  |  | NO | Link Code |
| HL7_ConnectedToEnsemble | varchar |  |  | SI | Connected To Ensemble |
| HL7_DateLastMessage | date |  |  | SI | Date of Last Message |
| HL7_DateStarted | date |  |  | SI | Date interface started |
| HL7_DateStopped | date |  |  | SI | Date interface stopped |
| HL7_DaysTraceKeep | double |  |  | SI | Number of days to keep trace |
| HL7_DefAdmDept_DR | bigint |  | FK | SI | Default Admission Dept_DR |
| HL7_DefAdmType | varchar |  |  | SI | Default Admission Type |
| HL7_DefRefDr_DR | bigint |  | FK | SI | Default Referring Doctor_Dr |
| HL7_DelimInMSH | varchar |  |  | SI | Delimiters In MSH |
| HL7_DeviceType | varchar |  |  | SI | Device Type |
| HL7_LineFeedAlternative | varchar |  |  | SI | Line Feed Separator Alternative |
| HL7_LocalApplication | varchar |  |  | SI | Local Application |
| HL7_MSHInboundExtCodeCheck | varchar |  |  | SI | Use MSH App and Fac to extract OrdItem code |
| HL7_MSHOutboundExtCodeCheck | varchar |  |  | SI | Use App and Fac against OrdItem in MSH |
| HL7_MarkAsRead | varchar |  |  | SI | Mark Results As Read |
| HL7_MessageCount | double |  |  | SI | Number of messages since last started |
| HL7_NameFields | varchar |  |  | SI | Name Fields |
| HL7_NameOfFacility | varchar |  |  | SI | Name Of Facility |
| HL7_PortRangeLower | double |  |  | SI | Port Range Lower |
| HL7_PortRangeUpper | double |  |  | SI | Port Range Upper |
| HL7_QueryInterface | varchar |  |  | SI | Query Interface |
| HL7_ReceivedResultSection | varchar |  |  | SI | Received Result Section |
| HL7_RemoteApplication | varchar |  |  | SI | Remote Application |
| HL7_RemoteFacilityName | varchar |  |  | SI | Remote Facility Name |
| HL7_RoutineSiteCodeInbound | varchar |  |  | SI | Inbound routine site code |
| HL7_RoutineSiteCodeOutbound | varchar |  |  | SI | Outbound routine site code |
| HL7_SegmentTimeout | varchar |  |  | SI | Segment Timeout |
| HL7_SendAA_ACK_error | varchar |  |  | SI | Send AA ACK if error |
| HL7_SendAdmissionRowId | varchar |  |  | SI | Send Admission RowId |
| HL7_SendProcessingMode | varchar |  |  | SI | Send Processing Mode |
| HL7_TimeLastMessage | time |  |  | SI | Time of Last Message |
| HL7_TimeStarted | time |  |  | SI | Time interface started |
| HL7_TimeStopped | time |  |  | SI | Time interface stopped |
| HL7_UpdateDate | date |  |  | SI | Update date |
| HL7_UpdateTime | time |  |  | SI | Update time |
| HL7_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HL7_UpdateUser_DR | bigint |  | FK | SI | Des Ref Update user |
| HL7_VerifUserCode | bigint |  |  | SI | Verif User Code |
| HL7_Version | varchar |  |  | SI | Version |
| HL7_WaitBeforeSend | varchar |  |  | SI | Wait Before Send |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*