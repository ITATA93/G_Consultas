# SQLUser.PAC_ContDelivMode

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTDELMODE_RowId | bigint | PK |  | NO | - |
| CONTDELMODE_Code | varchar |  |  | NO | Code |
| CONTDELMODE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTDELMODE_CreatedDate | date |  |  | SI | Created Date |
| CONTDELMODE_CreatedTime | time |  |  | SI | Created Time |
| CONTDELMODE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTDELMODE_DateFrom | date |  |  | SI | Date From |
| CONTDELMODE_DateTo | date |  |  | SI | Date To |
| CONTDELMODE_Desc | varchar |  |  | NO | Description |
| CONTDELMODE_Owner | varchar |  |  | SI | Owner |
| CONTDELMODE_UpdatedDate | date |  |  | SI | Updated Date |
| CONTDELMODE_UpdatedTime | time |  |  | SI | Updated Time |
| CONTDELMODE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of transport |
| Q04 | - |  |  | SI | Time of transport |
| Q05 | - |  |  | SI | Destination |
| Q06 | - |  |  | SI | Other destination |
| Q07 | - |  |  | SI | Patient secured for transport |
| Q08 | - |  |  | SI | Doctor |
| Q09 | - |  |  | SI | Nurse |
| Q10 | - |  |  | SI | Other |
| Q11 | - |  |  | SI | Escort notes |
| Q12 | - |  |  | SI | Electrocardiogram (ECG) |
| Q13 | - |  |  | SI | End-Tidal C02 (ETC02) |
| Q14 | - |  |  | SI | Arterial blood pressure |
| Q15 | - |  |  | SI | Oxygen saturation (SpO2) |
| Q16 | - |  |  | SI | Non-invasive blood pressure |
| Q17 | - |  |  | SI | Intracranial pressure / Cerebral perfusion pressur... |
| Q18 | - |  |  | SI | Monitoring notes |
| Q19 | - |  |  | SI | Model |
| Q19ObsDR | - |  |  | SI | Model DR |
| Q20 | - |  |  | SI | Mode |
| Q20ObsDR | - |  |  | SI | Mode DR |
| Q21 | - |  |  | SI | Set Insp Pressure (cmH2O) |
| Q21ObsDR | - |  |  | SI | Set Insp Pressure (cmH2O) DR |
| Q22 | - |  |  | SI | Set positive end expiratory pressure (cmH2O) |
| Q22ObsDR | - |  |  | SI | Set positive end expiratory pressure (cmH2O) DR |
| Q23 | - |  |  | SI | Set fraction of inspired oxygen (%) |
| Q23ObsDR | - |  |  | SI | Set fraction of inspired oxygen (%) DR |
| Q24 | - |  |  | SI | Set tidal volume  (mls) |
| Q24ObsDR | - |  |  | SI | Set tidal volume  (mls) DR |
| Q25 | - |  |  | SI | Set minute volume (L/min) |
| Q25ObsDR | - |  |  | SI | Set minute volume (L/min) DR |
| Q26 | - |  |  | SI | Transport ventilatory notes |
| Q27 | - |  |  | SI | Airway device |
| Q28 | - |  |  | SI | Endotracheal tube (ETT) size (mm) |
| Q28ObsDR | - |  |  | SI | Endotracheal tube (ETT) size (mm) DR |
| Q29 | - |  |  | SI | ETT length at lip (cm) |
| Q29ObsDR | - |  |  | SI | ETT length at lip (cm) DR |
| Q30 | - |  |  | SI | ETT length (cm) |
| Q30ObsDR | - |  |  | SI | ETT length (cm) DR |
| Q31 | - |  |  | SI | ETT measured at |
| Q31ObsDR | - |  |  | SI | ETT measured at DR |
| Q32 | - |  |  | SI | ETT cuff pressure (cmH20) |
| Q32ObsDR | - |  |  | SI | ETT cuff pressure (cmH20) DR |
| Q33 | - |  |  | SI | Tracheostomy type |
| Q33ObsDR | - |  |  | SI | Tracheostomy type DR |
| Q34 | - |  |  | SI | Tracheostomy tube size (mm) |
| Q34ObsDR | - |  |  | SI | Tracheostomy tube size (mm) DR |
| Q35 | - |  |  | SI | Tracheostomy cuff pressure (cmH20) |
| Q35ObsDR | - |  |  | SI | Tracheostomy cuff pressure (cmH20) DR |
| Q36 | - |  |  | SI | Airway and associated airway device(s) secure |
| Q37 | - |  |  | SI | Airway notes |
| Q38 | - |  |  | SI | Sedated or paralysed |
| Q39 | - |  |  | SI | Established on transport ventilator |
| Q40 | - |  |  | SI | Recent Arterial Blood Gas (ABG) |
| Q41 | - |  |  | SI | Intercostal Catheter (ICC) on suction |
| Q42 | - |  |  | SI | Breathing notes |
| Q43 | - |  |  | SI | Cardiovascular system stable |
| Q44 | - |  |  | SI | Haemoglobin > 70 (g/dl) |
| Q45 | - |  |  | SI | Sufficient vasopressor infusions |
| Q46 | - |  |  | SI | Intravascular access (IV) including emergency port |
| Q47 | - |  |  | SI | All IV lines visible and secure |
| Q48 | - |  |  | SI | Peripheral IV access (for contrast CT) |
| Q49 | - |  |  | SI | Circulation notes |
| Q50 | - |  |  | SI | Recent neuro observations documented and safe for ... |
| Q51 | - |  |  | SI | Pupillary size and response assessed |
| Q52 | - |  |  | SI | Blood Sugar Level (BSL) over 4 mmol/L |
| Q53 | - |  |  | SI | Cervical spine protected and documented |
| Q54 | - |  |  | SI | Disability notes |
| Q55 | - |  |  | SI | Temperature |
| Q55ObsDR | - |  |  | SI | Temperature DR |
| Q56 | - |  |  | SI | Patient stable and dignified |
| Q57 | - |  |  | SI | Drains functioning and secure |
| Q58 | - |  |  | SI | Exposure notes |
| Q59 | - |  |  | SI | Destination department aware patient is in transit |
| Q60 | - |  |  | SI | Relatives informed |
| Q61 | - |  |  | SI | Consultant and team leader aware of transfer |
| Q62 | - |  |  | SI | Destination department aware if additional precaut... |
| Q63 | - |  |  | SI | Examples: Methicillin Resistant Staphylococcus Aur... |
| Q64 | - |  |  | SI | Organisation notes |
| Q65 | - |  |  | SI | Resuscitation pack |
| Q66 | - |  |  | SI | Portable suction and tubing in working order |
| Q67 | - |  |  | SI | Patient slide sheet. To remain under patient on im... |
| Q68 | - |  |  | SI | Automated External Defibrillator (AED) |
| Q69 | - |  |  | SI | Paralysis medication |
| Q70 | - |  |  | SI | Extra sedation / Pain relief |
| Q71 | - |  |  | SI | Metaraminol |
| Q72 | - |  |  | SI | Bag valve mask resuscitator |
| Q73 | - |  |  | SI | Sufficient oxygen supplies |
| Q74 | - |  |  | SI | Inner cannula, spare tracheostomy tube and trachea... |
| Q75 | - |  |  | SI | Intra Aortic Balloon Pump (IABP) |
| Q76 | - |  |  | SI | Equipment notes |
| Q77 | - |  |  | SI | Additional intravascular line length as per protoc... |
| Q78 | - |  |  | SI | Silver dressings removed |
| Q79 | - |  |  | SI | Intracranial pressure monitor cable / sensor coile... |
| Q80 | - |  |  | SI | Foley temperature catheter removed |
| Q81 | - |  |  | SI | MRI patient checklist completed |
| Q82 | - |  |  | SI | MRI transport notes |
| Q83 | - |  |  | SI | As per minimum standard for inter-hospital transpo... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*