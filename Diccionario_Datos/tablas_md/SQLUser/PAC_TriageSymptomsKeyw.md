# SQLUser.PAC_TriageSymptomsKeyw

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | PAC_TriageSymptoms Parent Reference |
| ChildQ88DR | - |  |  | SI | Child Reference: Test doses |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Description | varchar |  |  | SI | Description |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_Text | varchar |  |  | SI | Text |
| Q58Q1 | - |  |  | SI | Insertion site checks |
| Q58Q2 | - |  |  | SI | Catheter check |
| Q58Q3 | - |  |  | SI | Dressing status |
| Q58Q4 | - |  |  | SI | Actions performed |
| Q58Q5 | - |  |  | SI | Assessment notes |
| Q58Q6 | - |  |  | SI | Assessment performed by |
| Q58Q7 | - |  |  | SI | Date |
| Q58Q8 | - |  |  | SI | Time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*