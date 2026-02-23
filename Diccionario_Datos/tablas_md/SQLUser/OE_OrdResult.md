# SQLUser.OE_OrdResult

**Schema:** SQLUser
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RES_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ68DR | - |  |  | SI | Child Reference: Compression garment requirements |
| Q66Q1 | - |  |  | SI | Date |
| Q66Q2 | - |  |  | SI | Weight |
| Q66Q3 | - |  |  | SI | Volume right |
| Q66Q4 | - |  |  | SI | Volume Left |
| Q66Q5 | - |  |  | SI | Difference |
| Q66Q6 | - |  |  | SI | Bioimpedance L-Dex score |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RES_Abnormal | varchar |  |  | SI | Abnormal |
| RES_Archive | varchar |  |  | SI | Archive |
| RES_CPReported_DR | varchar |  | FK | SI | Des Ref CPReported |
| RES_CPVerified_DR | varchar |  | FK | SI | Des Ref CPVerified |
| RES_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP (Doctor Entered) |
| RES_Childsub | double |  |  | NO | Childsub |
| RES_DICOM_PatientID | varchar |  |  | SI | DICOM Patient ID |
| RES_DICOM_SOPInstanceUID | varchar |  |  | SI | DICOM SOP InstanceUID (unique id for image) |
| RES_DICOM_SeriesInstanceUID | varchar |  |  | SI | DICOM Series Instance UID |
| RES_DICOM_SeriesModality | varchar |  |  | SI | DICOM Series Modality |
| RES_DICOM_SeriesNumber | varchar |  |  | SI | DICOM Series Number |
| RES_DICOM_StudyAccessionNo | varchar |  |  | SI | DICOM Study Accession No |
| RES_DICOM_StudyID | varchar |  |  | SI | DICOM Study ID |
| RES_DICOM_StudyInstanceUID | varchar |  |  | SI | DICOM Study Instance UID |
| RES_DateCreated | date |  |  | SI | Date Created |
| RES_DateRead | date |  |  | SI | Date Read |
| RES_DateUnread | date |  |  | SI | Date Unread |
| RES_DateVerified | date |  |  | SI | Date Verified |
| RES_DeliveryDate | date |  |  | SI | Delivery Date |
| RES_DeliveryTime | time |  |  | SI | Delivery Time |
| RES_Desc | varchar |  |  | SI | Description |
| RES_FileName | varchar |  |  | SI | File Name |
| RES_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| RES_LastUpdateHospital_DR | bigint |  | FK | SI | LastUpdateHospital |
| RES_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| RES_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| RES_Name | varchar |  |  | SI | Name |
| RES_NonSTDRepIssReason_DR | bigint |  | FK | SI | Des Ref NonSTDRepIssReason |
| RES_OverridePath | varchar |  |  | SI | Override Path |
| RES_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| RES_RecDep_DR | bigint |  | FK | SI | Des Ref RecDep |
| RES_ReportNotExpected | varchar |  |  | SI | Report Not Expected |
| RES_ResStat_DR | bigint |  | FK | SI | Des Ref ResultStatus |
| RES_RowId | varchar |  |  | NO | - |
| RES_Tag | varchar |  |  | SI | Tag |
| RES_Text | varchar |  |  | SI | Text |
| RES_TimeCreated | time |  |  | SI | Time Created |
| RES_TimeRead | time |  |  | SI | Time Read |
| RES_TimeUnread | time |  |  | SI | Time Unread |
| RES_TimeVerified | time |  |  | SI | Time Verified |
| RES_Type | varchar |  |  | SI | Result Type |
| RES_UserCreated | bigint |  |  | SI | User Created |
| RES_UserRead_DR | bigint |  | FK | SI | Des Ref UserRead |
| RES_UserTranscribed_DR | bigint |  | FK | SI | Des Ref UserTranscribed |
| RES_UserUnread_DR | bigint |  | FK | SI | Des Ref UserUnread |
| RES_UserVerified | bigint |  |  | SI | User Verified |
| RES_VoiceLength | double |  |  | SI | VoiceLength |
| RES_websysDocument | bigint |  |  | SI | websysDocument |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*