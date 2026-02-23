# questionnaire.QGXXXIVA

> Intravascular Access

**Schema:** questionnaire
**Columnas:** 198
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intravascular Access

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q04 | varchar |  |  | SI | Insertion reason |
| Q05 | varchar |  |  | SI | Explained procedure to patient and verified consen... |
| Q06 | varchar |  |  | SI | Prepared materials / documents / medications? |
| Q07 | varchar |  |  | SI | Insertion site assessed and marked if appropriate? |
| Q08 | varchar |  |  | SI | Assembled all necessary equipment |
| Q09 | varchar |  |  | SI | Patient positioned correctly? |
| Q10 | varchar |  |  | SI | All persons in the room had clean hands? |
| Q100 | varchar |  |  | SI | Catheter material |
| Q100ObsDR | varchar |  | FK | SI | Catheter material DR |
| Q101 | varchar |  |  | SI | Insertion site (peripheral) |
| Q101ObsDR | varchar |  | FK | SI | Insertion site (peripheral) DR |
| Q102 | varchar |  |  | SI | Insertion site (venous) |
| Q102ObsDR | varchar |  | FK | SI | Insertion site (venous) DR |
| Q103 | varchar |  |  | SI | Insertion site - implantable port |
| Q103ObsDR | varchar |  | FK | SI | Insertion site - implantable port DR |
| Q104 | varchar |  |  | SI | Catheter tip location |
| Q104ObsDR | varchar |  | FK | SI | Catheter tip location DR |
| Q105 | varchar |  |  | SI | Right atrial pressure (mmHg) |
| Q105ObsDR | varchar |  | FK | SI | Right atrial pressure (mmHg) DR |
| Q106 | varchar |  |  | SI | Right ventricular pressure (mmHg) |
| Q106ObsDR | varchar |  | FK | SI | Right ventricular pressure (mmHg) DR |
| Q107 | varchar |  |  | SI | Pulmonary artery pressure (mmHg) |
| Q107ObsDR | varchar |  | FK | SI | Pulmonary artery pressure (mmHg) DR |
| Q108 | varchar |  |  | SI | Length of IABP - insertion site to second hub (cm) |
| Q108ObsDR | varchar |  | FK | SI | Length of IABP - insertion site to second hub (cm)... |
| Q109 | varchar |  |  | SI | Immediate complications of insertion |
| Q11 | varchar |  |  | SI | Skin disinfected correctly? |
| Q110 | varchar |  |  | SI | Catheter and insertion comments |
| Q111 | varchar |  |  | SI | Operator |
| Q112 | varchar |  |  | SI | Assistant |
| Q113 | varchar |  |  | SI | Clinician |
| Q114 | varchar |  |  | SI | Insertion site (arterial) |
| Q114ObsDR | varchar |  | FK | SI | Insertion site (arterial) DR |
| Q115 | varchar |  |  | SI | Insertion site (intraosseous) |
| Q115ObsDR | varchar |  | FK | SI | Insertion site (intraosseous) DR |
| Q116 | date |  |  | SI | Date |
| Q117 | time |  |  | SI | Time |
| Q118 | varchar |  |  | SI | Pulmonary artery  occlusion pressure (mmHg) |
| Q118ObsDR | varchar |  | FK | SI | Pulmonary artery  occlusion pressure (mmHg) DR |
| Q119 | numeric |  |  | SI | Catheter length at wedge (cm) |
| Q12 | varchar |  |  | SI | Patient was covered from head to toe with a steril... |
| Q120 | varchar |  |  | SI | Indication for IABP |
| Q121 | varchar |  |  | SI | IABP Checklist |
| Q123 | varchar |  |  | SI | cm |
| Q124 | varchar |  |  | SI | cm |
| Q125 | varchar |  |  | SI | cm |
| Q126 | varchar |  |  | SI | cm |
| Q127 | varchar |  |  | SI | cm |
| Q128 | varchar |  |  | SI | Details of correction |
| Q129 | varchar |  |  | SI | Barcode |
| Q13 | varchar |  |  | SI | Used ultrasound guidance if appropriate? |
| Q130 | varchar |  |  | SI | Total days of insertion |
| Q131 | date |  |  | SI | Removal due date |
| Q132 | varchar |  |  | SI | Indication for haemodialysis catheter |
| Q134 | varchar |  |  | SI | Arterial lumen condition |
| Q135 | numeric |  |  | SI | Insertion length at skin (cm) |
| Q136 | varchar |  |  | SI | Notes |
| Q137 | varchar |  |  | SI | Staff |
| Q14 | varchar |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q15 | varchar |  |  | SI | Care provider and patient in the room wore masks? |
| Q16 | varchar |  |  | SI | Maintained sterile field? |
| Q17 | varchar |  |  | SI | Was sterile technique maintained when applying dre... |
| Q18 | varchar |  |  | SI | Was dressing dated? |
| Q19 | varchar |  |  | SI | Catheter position confirmed? |
| Q20 | varchar |  |  | SI | Daily review of line necessity? |
| Q21 | varchar |  |  | SI | Pre-procedure comments |
| Q22 | varchar |  |  | SI | Name of procedure CP |
| Q23 | varchar |  |  | SI | Name of assisting CP |
| Q24 | varchar |  |  | SI | Other clinician |
| Q25 | varchar |  |  | SI | Skin preparation |
| Q25a | varchar |  |  | SI | Note |
| Q26 | varchar |  |  | SI | Insertion technique |
| Q27 | varchar |  |  | SI | Checklist |
| Q28 | numeric |  |  | SI | Number of insertion attempts |
| Q29 | numeric |  |  | SI | PA catheter length |
| Q30 | varchar |  |  | SI | Information |
| Q31 | date |  |  | SI | Date inserted |
| Q32 | time |  |  | SI | Time inserted |
| Q33 | date |  |  | SI | Date infection found |
| Q34 | time |  |  | SI | Time infection found |
| Q35 | date |  |  | SI | Date infection heal up |
| Q36 | time |  |  | SI | Time infection heal up |
| Q37 | date |  |  | SI | Date removed |
| Q38 | time |  |  | SI | Time removed |
| Q39 | varchar |  |  | SI | Catheter type |
| Q39ObsDR | varchar |  | FK | SI | Catheter type DR |
| Q40 | varchar |  |  | SI | IV type |
| Q41 | varchar |  |  | SI | IABP manufacturer / model |
| Q41N | varchar |  |  | SI | Note IABP |
| Q41S | varchar |  |  | SI | Size |
| Q41V | varchar |  |  | SI | Balloon volume |
| Q42 | varchar |  |  | SI | PA type |
| Q43 | varchar |  |  | SI | Localisation |
| Q43ObsDR | varchar |  | FK | SI | Localisation DR |
| Q44 | varchar |  |  | SI | Insertion side |
| Q44ObsDR | varchar |  | FK | SI | Insertion side DR |
| Q45 | varchar |  |  | SI | Size / Color |
| Q45ObsDR | varchar |  | FK | SI | Size / Color DR |
| Q46 | varchar |  |  | SI | Characteristics |
| Q46ObsDR | varchar |  | FK | SI | Characteristics DR |
| Q47 | varchar |  |  | SI | Material |
| Q47ObsDR | varchar |  | FK | SI | Material DR |
| Q48 | varchar |  |  | SI | Position |
| Q48ObsDR | varchar |  | FK | SI | Position DR |
| Q49 | varchar |  |  | SI | Easy localisation |
| Q50 | varchar |  |  | SI | IV access labeled with date inserted |
| Q51 | varchar |  |  | SI | IV access labeled with name and change due |
| Q53 | varchar |  |  | SI | Flush bag labeled with date and time |
| Q54 | varchar |  |  | SI | Flush bag pressure checked |
| Q56 | varchar |  |  | SI | Local anaesthetic used |
| Q57 | varchar |  |  | SI | Removal type |
| Q58 | varchar |  |  | SI | Informed consent obtained from patient? |
| Q59 | varchar |  |  | SI | Total days of insertion |
| Q60 | varchar |  |  | SI | Barrier precautions used |
| Q61 | varchar |  |  | SI | Hair removal, if required, using disposable clippe... |
| Q62 | varchar |  |  | SI | Skin preparation used |
| Q63 | varchar |  |  | SI | Catheter flushed before insertion |
| Q64 | varchar |  |  | SI | Vessel identification techniques |
| Q65 | varchar |  |  | SI | Catheter brand / model / lot number |
| Q66 | numeric |  |  | SI | Total catheter length (cm) |
| Q67 | numeric |  |  | SI | Catheter internal length (cm) |
| Q68 | numeric |  |  | SI | Catheter exposed length (cm) |
| Q69 | numeric |  |  | SI | Number of lumens |
| Q70 | varchar |  |  | SI | Distal lumen orifice |
| Q72 | varchar |  |  | SI | Tunnelled |
| Q73 | varchar |  |  | SI | Cuffed |
| Q74 | varchar |  |  | SI | Coating / Impregnation |
| Q75 | varchar |  |  | SI | Catheter secured by |
| Q76 | varchar |  |  | SI | Catheter position confirmation |
| Q77 | varchar |  |  | SI | Incorrect position corrected by |
| Q78 | varchar |  |  | SI | Catheter label  |
| Q79 | varchar |  |  | SI | PAC checklist |
| Q7z1 | varchar |  |  | SI | Catheter body |
| Q80 | varchar |  |  | SI | PAC Measurements |
| Q81 | varchar |  |  | SI | Computational constant |
| Q81ObsDR | varchar |  | FK | SI | Computational constant DR |
| Q82 | varchar |  |  | SI | Insertion site check |
| Q83 | varchar |  |  | SI | Visual phlebitis score |
| Q86 | date |  |  | SI | Removal date |
| Q87 | time |  |  | SI | Removal time |
| Q88 | varchar |  |  | SI | Removal reason |
| Q89 | varchar |  |  | SI | Catheter tip sent for culture |
| Q90 | varchar |  |  | SI | Catheter removal comments |
| Q91 | varchar |  |  | SI | Catheter removed by |
| Q92 | varchar |  |  | SI | Catheter complications and defect type |
| Q93 | varchar |  |  | SI | Catheter complication comments |
| Q94 | varchar |  |  | SI | Catheter type |
| Q95 | varchar |  |  | SI | Size / gauge - peripheral |
| Q95ObsDR | varchar |  | FK | SI | Size / gauge - peripheral DR |
| Q96 | varchar |  |  | SI | Size / gauge - central venous or arterial |
| Q96ObsDR | varchar |  | FK | SI | Size / gauge - central venous or arterial DR |
| Q97 | varchar |  |  | SI | Size / gauge - intraosseous needle |
| Q97ObsDR | varchar |  | FK | SI | Size / gauge - intraosseous needle DR |
| Q98 | varchar |  |  | SI | IABP balloon size |
| Q98ObsDR | varchar |  | FK | SI | IABP balloon size DR |
| Q99 | varchar |  |  | SI | Needle length required for accessing implantable p... |
| Q99ObsDR | varchar |  | FK | SI | Needle length required for accessing implantable p... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*