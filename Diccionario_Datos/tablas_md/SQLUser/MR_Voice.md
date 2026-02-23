# SQLUser.MR_Voice

**Schema:** SQLUser
**Columnas:** 206
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VOI_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ85DR | - |  |  | SI | Child Reference: IABP Checks |
| Q04 | - |  |  | SI | Insertion reason |
| Q05 | - |  |  | SI | Explained procedure to patient and verified consen... |
| Q06 | - |  |  | SI | Prepared materials / documents / medications? |
| Q07 | - |  |  | SI | Insertion site assessed and marked if appropriate? |
| Q08 | - |  |  | SI | Assembled all necessary equipment |
| Q09 | - |  |  | SI | Patient positioned correctly? |
| Q10 | - |  |  | SI | All persons in the room had clean hands? |
| Q100 | - |  |  | SI | Catheter material |
| Q100ObsDR | - |  |  | SI | Catheter material DR |
| Q101 | - |  |  | SI | Insertion site (peripheral) |
| Q101ObsDR | - |  |  | SI | Insertion site (peripheral) DR |
| Q102 | - |  |  | SI | Insertion site (venous) |
| Q102ObsDR | - |  |  | SI | Insertion site (venous) DR |
| Q103 | - |  |  | SI | Insertion site - implantable port |
| Q103ObsDR | - |  |  | SI | Insertion site - implantable port DR |
| Q104 | - |  |  | SI | Catheter tip location |
| Q104ObsDR | - |  |  | SI | Catheter tip location DR |
| Q105 | - |  |  | SI | Right atrial pressure (mmHg) |
| Q105ObsDR | - |  |  | SI | Right atrial pressure (mmHg) DR |
| Q106 | - |  |  | SI | Right ventricular pressure (mmHg) |
| Q106ObsDR | - |  |  | SI | Right ventricular pressure (mmHg) DR |
| Q107 | - |  |  | SI | Pulmonary artery pressure (mmHg) |
| Q107ObsDR | - |  |  | SI | Pulmonary artery pressure (mmHg) DR |
| Q108 | - |  |  | SI | Length of IABP - insertion site to second hub (cm) |
| Q108ObsDR | - |  |  | SI | Length of IABP - insertion site to second hub (cm)... |
| Q109 | - |  |  | SI | Immediate complications of insertion |
| Q11 | - |  |  | SI | Skin disinfected correctly? |
| Q110 | - |  |  | SI | Catheter and insertion comments |
| Q111 | - |  |  | SI | Operator |
| Q112 | - |  |  | SI | Assistant |
| Q113 | - |  |  | SI | Clinician |
| Q114 | - |  |  | SI | Insertion site (arterial) |
| Q114ObsDR | - |  |  | SI | Insertion site (arterial) DR |
| Q115 | - |  |  | SI | Insertion site (intraosseous) |
| Q115ObsDR | - |  |  | SI | Insertion site (intraosseous) DR |
| Q116 | - |  |  | SI | Date |
| Q117 | - |  |  | SI | Time |
| Q118 | - |  |  | SI | Pulmonary artery  occlusion pressure (mmHg) |
| Q118ObsDR | - |  |  | SI | Pulmonary artery  occlusion pressure (mmHg) DR |
| Q119 | - |  |  | SI | Catheter length at wedge (cm) |
| Q12 | - |  |  | SI | Patient was covered from head to toe with a steril... |
| Q120 | - |  |  | SI | Indication for IABP |
| Q121 | - |  |  | SI | IABP Checklist |
| Q123 | - |  |  | SI | cm |
| Q124 | - |  |  | SI | cm |
| Q125 | - |  |  | SI | cm |
| Q126 | - |  |  | SI | cm |
| Q127 | - |  |  | SI | cm |
| Q128 | - |  |  | SI | Details of correction |
| Q129 | - |  |  | SI | Barcode |
| Q13 | - |  |  | SI | Used ultrasound guidance if appropriate? |
| Q130 | - |  |  | SI | Total days of insertion |
| Q131 | - |  |  | SI | Removal due date |
| Q132 | - |  |  | SI | Indication for haemodialysis catheter |
| Q134 | - |  |  | SI | Arterial lumen condition |
| Q135 | - |  |  | SI | Insertion length at skin (cm) |
| Q136 | - |  |  | SI | Notes |
| Q137 | - |  |  | SI | Staff |
| Q14 | - |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q15 | - |  |  | SI | Care provider and patient in the room wore masks? |
| Q16 | - |  |  | SI | Maintained sterile field? |
| Q17 | - |  |  | SI | Was sterile technique maintained when applying dre... |
| Q18 | - |  |  | SI | Was dressing dated? |
| Q19 | - |  |  | SI | Catheter position confirmed? |
| Q20 | - |  |  | SI | Daily review of line necessity? |
| Q21 | - |  |  | SI | Pre-procedure comments |
| Q22 | - |  |  | SI | Name of procedure CP |
| Q23 | - |  |  | SI | Name of assisting CP |
| Q24 | - |  |  | SI | Other clinician |
| Q25 | - |  |  | SI | Skin preparation |
| Q25a | - |  |  | SI | Note |
| Q26 | - |  |  | SI | Insertion technique |
| Q27 | - |  |  | SI | Checklist |
| Q28 | - |  |  | SI | Number of insertion attempts |
| Q29 | - |  |  | SI | PA catheter length |
| Q30 | - |  |  | SI | Information |
| Q31 | - |  |  | SI | Date inserted |
| Q32 | - |  |  | SI | Time inserted |
| Q33 | - |  |  | SI | Date infection found |
| Q34 | - |  |  | SI | Time infection found |
| Q35 | - |  |  | SI | Date infection heal up |
| Q36 | - |  |  | SI | Time infection heal up |
| Q37 | - |  |  | SI | Date removed |
| Q38 | - |  |  | SI | Time removed |
| Q39 | - |  |  | SI | Catheter type |
| Q39ObsDR | - |  |  | SI | Catheter type DR |
| Q40 | - |  |  | SI | IV type |
| Q41 | - |  |  | SI | IABP manufacturer / model |
| Q41N | - |  |  | SI | Note IABP |
| Q41S | - |  |  | SI | Size |
| Q41V | - |  |  | SI | Balloon volume |
| Q42 | - |  |  | SI | PA type |
| Q43 | - |  |  | SI | Localisation |
| Q43ObsDR | - |  |  | SI | Localisation DR |
| Q44 | - |  |  | SI | Insertion side |
| Q44ObsDR | - |  |  | SI | Insertion side DR |
| Q45 | - |  |  | SI | Size / Color |
| Q45ObsDR | - |  |  | SI | Size / Color DR |
| Q46 | - |  |  | SI | Characteristics |
| Q46ObsDR | - |  |  | SI | Characteristics DR |
| Q47 | - |  |  | SI | Material |
| Q47ObsDR | - |  |  | SI | Material DR |
| Q48 | - |  |  | SI | Position |
| Q48ObsDR | - |  |  | SI | Position DR |
| Q49 | - |  |  | SI | Easy localisation |
| Q50 | - |  |  | SI | IV access labeled with date inserted |
| Q51 | - |  |  | SI | IV access labeled with name and change due |
| Q53 | - |  |  | SI | Flush bag labeled with date and time |
| Q54 | - |  |  | SI | Flush bag pressure checked |
| Q56 | - |  |  | SI | Local anaesthetic used |
| Q57 | - |  |  | SI | Removal type |
| Q58 | - |  |  | SI | Informed consent obtained from patient? |
| Q59 | - |  |  | SI | Total days of insertion |
| Q60 | - |  |  | SI | Barrier precautions used |
| Q61 | - |  |  | SI | Hair removal, if required, using disposable clippe... |
| Q62 | - |  |  | SI | Skin preparation used |
| Q63 | - |  |  | SI | Catheter flushed before insertion |
| Q64 | - |  |  | SI | Vessel identification techniques |
| Q65 | - |  |  | SI | Catheter brand / model / lot number |
| Q66 | - |  |  | SI | Total catheter length (cm) |
| Q67 | - |  |  | SI | Catheter internal length (cm) |
| Q68 | - |  |  | SI | Catheter exposed length (cm) |
| Q69 | - |  |  | SI | Number of lumens |
| Q70 | - |  |  | SI | Distal lumen orifice |
| Q72 | - |  |  | SI | Tunnelled |
| Q73 | - |  |  | SI | Cuffed |
| Q74 | - |  |  | SI | Coating / Impregnation |
| Q75 | - |  |  | SI | Catheter secured by |
| Q76 | - |  |  | SI | Catheter position confirmation |
| Q77 | - |  |  | SI | Incorrect position corrected by |
| Q78 | - |  |  | SI | Catheter label |
| Q79 | - |  |  | SI | PAC checklist |
| Q7z1 | - |  |  | SI | Catheter body |
| Q80 | - |  |  | SI | PAC Measurements |
| Q81 | - |  |  | SI | Computational constant |
| Q81ObsDR | - |  |  | SI | Computational constant DR |
| Q82 | - |  |  | SI | Insertion site check |
| Q83 | - |  |  | SI | Visual phlebitis score |
| Q86 | - |  |  | SI | Removal date |
| Q87 | - |  |  | SI | Removal time |
| Q88 | - |  |  | SI | Removal reason |
| Q89 | - |  |  | SI | Catheter tip sent for culture |
| Q90 | - |  |  | SI | Catheter removal comments |
| Q91 | - |  |  | SI | Catheter removed by |
| Q92 | - |  |  | SI | Catheter complications and defect type |
| Q93 | - |  |  | SI | Catheter complication comments |
| Q94 | - |  |  | SI | Catheter type |
| Q95 | - |  |  | SI | Size / gauge - peripheral |
| Q95ObsDR | - |  |  | SI | Size / gauge - peripheral DR |
| Q96 | - |  |  | SI | Size / gauge - central venous or arterial |
| Q96ObsDR | - |  |  | SI | Size / gauge - central venous or arterial DR |
| Q97 | - |  |  | SI | Size / gauge - intraosseous needle |
| Q97ObsDR | - |  |  | SI | Size / gauge - intraosseous needle DR |
| Q98 | - |  |  | SI | IABP balloon size |
| Q98ObsDR | - |  |  | SI | IABP balloon size DR |
| Q99 | - |  |  | SI | Needle length required for accessing implantable p... |
| Q99ObsDR | - |  |  | SI | Needle length required for accessing implantable p... |
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
| VOI_Childsub | double |  |  | NO | Childsub |
| VOI_DateCreated | date |  |  | SI | Date Created |
| VOI_Desc | varchar |  |  | SI | Description |
| VOI_Path | varchar |  |  | SI | Path |
| VOI_RowId | varchar |  |  | NO | - |
| VOI_TimeCreated | time |  |  | SI | Time Created |
| VOI_UserCreated | bigint |  |  | SI | User Created |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*