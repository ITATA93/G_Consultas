# SQLUser.NRC_Intervention

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCI_RowID | bigint | PK |  | NO | - |
| ChildQ133DR | - |  |  | SI | Child Reference: Haemodialysis shift assessment |
| NRCI_Code | varchar |  |  | NO | Code  |
| NRCI_CodeTableTags | varchar |  |  | SI | List of code table tags |
| NRCI_DateFrom | date |  |  | NO | Effective date for the record |
| NRCI_DateTo | date |  |  | SI | Last day the record is active |
| NRCI_Definition | varchar |  |  | SI | Free Text Definition is a Long Description |
| NRCI_Desc | varchar |  |  | NO | Description |
| NRCI_Narrative | longvarchar |  |  | SI | Narrative Stream  |
| NRCI_Owner | varchar |  |  | SI | Owner |
| NRCI_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| NRCI_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| Q122Q1 | - |  |  | SI | Date |
| Q122Q2 | - |  |  | SI | Time |
| Q122Q3 | - |  |  | SI | Catheter check |
| Q122Q4 | - |  |  | SI | Dressing status |
| Q122Q5 | - |  |  | SI | Insertion site check |
| Q122Q6 | - |  |  | SI | Visual phlebitis score |
| Q122Q7 | - |  |  | SI | Actions |
| Q122Q8 | - |  |  | SI | Comments |
| Q122Q9 | - |  |  | SI | Staff |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*