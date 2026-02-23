# questionnaire.QTCEPSI

> Pauta de Seguridad Infantil

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta de Seguridad Infantil

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Medicamentos al alcance de los niños |
| Q02 | varchar |  |  | SI | Detergentes, veneno, cloro al alcance de los niños |
| Q03 | varchar |  |  | SI | Materiales de construcción al alcance de los niños |
| Q04 | varchar |  |  | SI | Basureros al alcance de los niños |
| Q05 | varchar |  |  | SI | Calefón sin tubo extractor |
| Q06 | varchar |  |  | SI | Estufas, braseros en ambientes no ventilados |
| Q07 | varchar |  |  | SI | Bolsas plásticas al alcance de los niños |
| Q08 | varchar |  |  | SI | Plantas dentro del hogar |
| Q09 | varchar |  |  | SI | Conexiones de gas al alcance de los niños |
| Q10 | varchar |  |  | SI | Productos tóxicos en botellas de bebidas |
| Q11 | varchar |  |  | SI | Escaleras sin protección (puertas de seguridad) |
| Q12 | varchar |  |  | SI | Puertas divisorias de vidrio sin señalización |
| Q13 | varchar |  |  | SI | Balcones sin protección (sin mallas de segurdad) |
| Q14 | varchar |  |  | SI | Ventanas sin protección (sin mallas de seguridad) |
| Q15 | varchar |  |  | SI | Muebles cerca de las ventanas |
| Q16 | varchar |  |  | SI | Mesas bajas con esquinas punteagudas |
| Q17 | varchar |  |  | SI | Puertas batientes |
| Q18 | varchar |  |  | SI | Materiales de costura al alcance de los niños |
| Q19 | varchar |  |  | SI | Utensilios de cocina al alcance de los niños |
| Q20 | varchar |  |  | SI | Pisos resbaladizos al limpiarlos (tener precaución... |
| Q21 | varchar |  |  | SI | Alfombras no adheridas al suelo o sueltas |
| Q22 | varchar |  |  | SI | Rejas con barrotes de separación suficiente, para ... |
| Q23 | varchar |  |  | SI | Mangos de ollas hacia fuera mientras se cocina |
| Q24 | varchar |  |  | SI | Enchufes sin protección |
| Q25 | varchar |  |  | SI | Conexiones eléctricas defectuosas |
| Q26 | varchar |  |  | SI | Libre entrada a la cocina en hora de preparación d... |
| Q27 | varchar |  |  | SI | Fósforos al alcance de los niños |
| Q28 | varchar |  |  | SI | Chimeneas sin protección  |
| Q29 | varchar |  |  | SI | Estufas, braseros o anafres en pasillos o sitio de... |
| Q30 | varchar |  |  | SI | Planchas enchufadas al alcance de lo sniños |
| Q31 | varchar |  |  | SI | Mesa con manteles largos |
| Q32 | varchar |  |  | SI | Juguetes de los hermanos mayores con partes pequeñ... |
| Q33 | varchar |  |  | SI | Objetos afilados como prendedores, aros, alfileres... |
| Q34 | varchar |  |  | SI | Armas de fuego al alcance de los niños |
| Q35 | varchar |  |  | SI | Puertas con seguro interno (se podrían encerrar co... |
| Q36 | varchar |  |  | SI | Acequias o canales cerca de la casa sin protección |
| Q37 | varchar |  |  | SI | Piscinas sin protección |
| Q38 | varchar |  |  | SI | Muebles móviles especialmente aquellos con objetos... |
| Q39 | varchar |  |  | SI | Cocina no fijada a la pared |
| Q40 | varchar |  |  | SI | Hervidores eléctricos con cable al alcance del niñ... |
| Q41 | varchar |  |  | SI | Transporte del niño o niña en vehículo sin  silla ... |
| Q42 | varchar |  |  | SI | Hemos tomado las siguientes medidas frente a los p... |
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