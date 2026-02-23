# SQLUser.LB_InstrumentTest

**Schema:** SQLUser
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBIT_RowID | bigint | PK |  | NO | - |
| ChildQ71DR | - |  |  | SI | Child Reference: Extremidades |
| LBIT_Active | varchar |  |  | SI | Flag to indicate if at least one of the results in... |
| LBIT_Comments | varchar |  |  | SI | Specimen container comments |
| LBIT_DateOfBirth | date |  |  | SI | POCT Date Of Birth
Cache Date |
| LBIT_FirstName | varchar |  |  | SI | POCT First Name |
| LBIT_InstrumentSpecimenID | varchar |  |  | NO | Specimen ID as provided by the instrument |
| LBIT_InstrumentTestGroups | varchar |  |  | SI | Link to the instrument test groups the results bel... |
| LBIT_Instrument_DR | bigint |  | FK | NO | Instrument the test is filed for: middleware or st... |
| LBIT_LastName | varchar |  |  | SI | POCT Last Name |
| LBIT_MRN | varchar |  |  | SI | POCT MRN |
| LBIT_MiddleName | varchar |  |  | SI | POCT Middle Name |
| LBIT_NationalID | varchar |  |  | SI | POCT National ID |
| LBIT_NumberOfRepeats | varchar |  |  | SI | Number of repeats |
| LBIT_PerformedOnInstrument_DR | bigint |  | FK | NO | Instrument the test was performed on 
Middleware,... |
| LBIT_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material the test was performed on |
| LBIT_QCRun_DR | bigint |  | FK | SI | Link to the QC Run |
| LBIT_Reagents | varchar |  |  | SI | Link to the instrument's reagents which were activ... |
| LBIT_RequestSpecimenContainer_DR | bigint |  | FK | SI | Request Specimen container the test was performed ... |
| LBIT_Sex | varchar |  |  | SI | POCT Sex
Sex Code |
| LBIT_SpecimenContainer_DR | bigint |  | FK | SI | Specimen container the test was performed on |
| LBIT_TestSets | varchar |  |  | SI | List of test sets the instrument test has already ... |
| LBIT_TransmissionDate | date |  |  | NO | Date test was transmitted |
| LBIT_TransmissionTime | time |  |  | NO | Time test was transmitted |
| LBIT_URN | varchar |  |  | SI | POCT URN |
| LBIT_UpdateDate | date |  |  | SI | Date of last update |
| LBIT_UpdateTime | time |  |  | SI | Time of last update |
| LBTI_Diluted | varchar |  |  | SI | Flag that indicates that the sample the test was p... |
| LBTI_DilutionFactor | numeric |  |  | SI | Dilution factor of the sample the test was perform... |
| Q64Q1 | - |  |  | SI | Palpación |
| Q64Q2 | - |  |  | SI | Percusión |
| Q64Q3 | - |  |  | SI | Auscultación |
| Q64Q4 | - |  |  | SI | Localización |
| Q64Q5 | - |  |  | SI | Lateralidad |
| Q64Q6 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*