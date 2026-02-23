# web_Msg.LBC_Instrument

**Schema:** web_Msg
**Columnas:** 49
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCIN_BloodPackDINLabel_DR | bigint |  | FK | SI | The report to use to produce the barcode-label of ... |
| LBCIN_Code | varchar |  |  | SI | Instrument Code
Required by User.LBCInstrument. |
| LBCIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCIN_ControlledByInstrument_DR | bigint |  | FK | SI | Instrument is controlled by another instrument
On... |
| LBCIN_CreatedDate | date |  |  | SI | Created Date |
| LBCIN_CreatedTime | time |  |  | SI | Created Time |
| LBCIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCIN_DateCommissioning | date |  |  | SI | Date of commissioning |
| LBCIN_DateDecommissioning | date |  |  | SI | Date of de-commissioning |
| LBCIN_DateFrom | date |  |  | SI | Date From |
| LBCIN_DateReceiptEquipment | date |  |  | SI | Date of receipt of equipment |
| LBCIN_DateTo | date |  |  | SI | Date To |
| LBCIN_Department_DR | bigint |  | FK | SI | Department
Required by User.LBCInstrument. |
| LBCIN_Desc | varchar |  |  | SI | Instrument Description
HTMLTextBox
Required by U... |
| LBCIN_DeviceIndicator | varchar |  |  | SI | Unique device indicator |
| LBCIN_DisplayStatusMsgOnSpecRec | varchar |  |  | SI | Display status message at specimen receive |
| LBCIN_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBCIN_InstrumentID | varchar |  |  | SI | The instrument ID the analyser is known by the mid... |
| LBCIN_InstrumentInterfaceNamespace | varchar |  |  | SI | Namespace of the instrument interface production |
| LBCIN_InstrumentType | varchar |  |  | SI | Type of the instrument
Standard type: LabInstrume... |
| LBCIN_InterfaceType | varchar |  |  | SI | Type of the instrument interface
Standard type: L... |
| LBCIN_LabAssetNumber | varchar |  |  | SI | Unique laboratory asset number |
| LBCIN_LabSite_DR | bigint |  | FK | SI | Lab Site (Location)
For POCT instruments that is ... |
| LBCIN_ManufacturerName | varchar |  |  | SI | Manufacturer Name |
| LBCIN_Model | varchar |  |  | SI | Model |
| LBCIN_Owner | varchar |  |  | SI | Owner |
| LBCIN_POCTCareProvider_DR | varchar |  | FK | SI | POCT Ordering Care Provider |
| LBCIN_POCTLocation_DR | bigint |  | FK | SI | POCT Location, the physical location of the POCT i... |
| LBCIN_POCTSpeciality_DR | bigint |  | FK | SI | POCT Speciality, the execute location of the POCT ... |
| LBCIN_QCBracketDuration | integer |  |  | SI | QC Bracket Duration |
| LBCIN_QCBracketDurationUnit | varchar |  |  | SI | QC Bracket Duration unit |
| LBCIN_QCBracketNumEpisodes | integer |  |  | SI | QC Bracket Number Of Samples |
| LBCIN_QCBracketing | varchar |  |  | SI | Instrument QC Bracketing
Standard type: LabInstru... |
| LBCIN_QCMode | varchar |  |  | SI | Instrument QC Mode
Standard type: LabInstrumentQC... |
| LBCIN_QCRunStartTime | time |  |  | SI | Start time of the daily run
Only used for Instrum... |
| LBCIN_RowID | varchar |  |  | SI | - |
| LBCIN_SerialNumber | varchar |  |  | SI | Serial Number |
| LBCIN_StatusMessage | varchar |  |  | SI | User Defined Status Message |
| LBCIN_TransmitsInstrumentIDs | varchar |  |  | SI | The middleware instrument transmits instrument IDs... |
| LBCIN_UpdatedDate | date |  |  | SI | Updated Date |
| LBCIN_UpdatedTime | time |  |  | SI | Updated Time |
| LBCIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCIN_UseSpecimenID | varchar |  |  | SI | Instrument uses Specimen IDs
Yes: reconcile is do... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*