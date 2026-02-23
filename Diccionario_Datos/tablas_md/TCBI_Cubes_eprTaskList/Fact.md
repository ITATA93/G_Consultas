# TCBI_Cubes_eprTaskList.Fact

**Schema:** TCBI_Cubes_eprTaskList
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| DxAdminStatus | bigint |  |  | SI | Dimension: DxAdminStatus
Expression: ##class(TCBI... |
| DxAssignedDate | date |  |  | SI | Dimension: DxAssignedDate<br/>
Source: AssignedDa... |
| DxAssignedDay | varchar |  |  | SI | Dimension: DxAssignedDay<br/>
Source: AssignedDat... |
| DxAssignedHospDR | bigint |  | FK | SI | Dimension: DxAssignedHospDR<br/>
Source: Assigned... |
| DxAssignedMonth | varchar |  |  | SI | Dimension: DxAssignedMonth<br/>
Source: AssignedD... |
| DxAssignedUserDR | bigint |  | FK | SI | Dimension: DxAssignedUserDR<br/>
Source: Assigned... |
| DxAssignedYear | varchar |  |  | SI | Dimension: DxAssignedYear<br/>
Source: AssignedDa... |
| DxExecutionDate | date |  |  | SI | Dimension: DxExecutionDate<br/>
Source: Execution... |
| DxExecutionDay | varchar |  |  | SI | Dimension: DxExecutionDay<br/>
Source: ExecutionD... |
| DxExecutionMonth | varchar |  |  | SI | Dimension: DxExecutionMonth<br/>
Source: Executio... |
| DxExecutionYear | varchar |  |  | SI | Dimension: DxExecutionYear<br/>
Source: Execution... |
| DxPriorityDR | bigint |  | FK | SI | Dimension: DxPriorityDR<br/>
Source: PriorityDR.O... |
| DxScheduledDate | date |  |  | SI | Dimension: DxScheduledDate<br/>
Source: Scheduled... |
| DxScheduledDay | varchar |  |  | SI | Dimension: DxScheduledDay<br/>
Source: ScheduledD... |
| DxScheduledMonth | varchar |  |  | SI | Dimension: DxScheduledMonth<br/>
Source: Schedule... |
| DxScheduledYear | varchar |  |  | SI | Dimension: DxScheduledYear<br/>
Source: Scheduled... |
| DxTaskDispositionDR | bigint |  | FK | SI | Dimension: DxTaskDispositionDR<br/>
Source: TaskD... |
| DxTaskItemDR | bigint |  | FK | SI | Dimension: DxTaskItemDR<br/>
Source: TaskItemDR.D... |
| DxUserGroupDR | bigint |  | FK | SI | Dimension: DxUserGroupDR<br/>
Source: UserGroupDR... |
| RxIDViaPAAdmDR | bigint |  | FK | SI | Relationship: RxIDViaPAAdmDR<br/>
Source: PAAdmDR... |
| RxIDViaPAPMIDR | bigint |  | FK | SI | Relationship: RxIDViaPAPMIDR<br/>
Source: PAPMIDR... |
| RxIDViaPAWaitingListDR | bigint |  | FK | SI | Relationship: RxIDViaPAWaitingListDR<br/>
Source:... |
| RxIDViaRBAppointmentDR | bigint |  | FK | SI | Relationship: RxIDViaRBAppointmentDR<br/>
Source:... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*