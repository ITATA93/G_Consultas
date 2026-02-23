# SQLUser.OE_OrdTeeth

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TEETH_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ27DR | - |  |  | SI | Child Reference: Coordination |
| Q26Q1 | - |  |  | SI | Location |
| Q26Q2 | - |  |  | SI | Criteria |
| Q26Q3 | - |  |  | SI | Score |
| Q26Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TEETH_Childsub | double |  |  | NO | Childsub |
| TEETH_RowId | varchar |  |  | NO | - |
| TEETH_ToothArea_DR | bigint |  | FK | SI | DR OEC_ToothArea |
| TEETH_ToothNum_DR | bigint |  | FK | SI | Des Ref to ToothNum |
| TEETH_ToothPosit_DR | bigint |  | FK | SI | Des Ref to ToothPosit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*